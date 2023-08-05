import functools
import inspect
import os
import pytest
from testit_adapter_pytest import utils as testit
from jira import JIRA

__all__ = [
    "check",
    "equal",
    "not_equal",
    "is_true",
    "is_false",
    "is_none",
    "is_not_none",
    "is_in",
    "is_not_in",
    "greater",
    "greater_equal",
    "less",
    "less_equal",
    "check_func",
    "check_dict_values",
    "check_status_code"
]


_stop_on_fail = False
_failures = []
_jira = None


@pytest.fixture(scope="function")
def connect_to_jira(request):
    _jira = JIRA(server=os.environ.get('JIRA_SERVER'), token_auth=os.environ.get('JIRA_TOKEN'))
    # _jira = JIRA(server="https://jira.zyfra.com", token_auth="PDfVwrnTO67ULw2BR4iQIdDktGInPf07jxxCqg")


def clear_failures():
    global _failures
    _failures = []


def get_failures():
    return _failures


def set_stop_on_fail(stop_on_fail):
    global _stop_on_fail
    _stop_on_fail = stop_on_fail


class CheckContextManager(object):
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        __tracebackhide__ = True
        if exc_type is not None and issubclass(exc_type, AssertionError):
            if _stop_on_fail:
                return
            else:
                log_failure(exc_val)
                return True


check = CheckContextManager()


def check_func(func):
    @functools.wraps(func)
    def wrapper(*args, **kwds):
        __tracebackhide__ = True
        try:
            func(*args, **kwds)
            return True
        except AssertionError as e:
            if _stop_on_fail:
                if kwds.get('bug_link'):
                    issue_info = _jira.issue(
                        kwds.get('bug_link'),
                        fields="created, status, fixVersions, priority, resolutiondate")
                    check_issue(issue_info, e)
                log_failure(e)
                raise e
            if kwds.get('bug_link'):
                issue_info = _jira.issue(
                    kwds.get('bug_link'),
                    fields="created, status, fixVersions, priority, resolutiondate")
                check_issue(issue_info, e)
            else:
                log_failure(e)
            return False

    return wrapper


@check_func
def equal(
        actual_value: any,
        expected_value: any,
        msg: str = None,
        stop_on_fail: bool = False,
        bug_link: str = None):
    """
    Проверить, что два значения равны. \n
    :param actual_value: фактическое значение.
    :param expected_value: ожидаемое значение.
    :param msg: сообщение об ошибке. По умолчанию используется сообщение вида:
     'Ошибка! Фактическое значение должно быть равно ожидаемому.\n
     Фактическое значение = '{actual_value}',\n
     Ожидаемое значение = '{expected_value}'.'
    :param bug_link: ссылка на баг. По умолчанию = None.
    :param stop_on_fail: параметр, отвечающий за необходимость фейлить тест после первой проваленной проверки.
     По умолчанию = False.
    """
    set_stop_on_fail(stop_on_fail)
    if not msg:
        msg = "\nОшибка! Фактическое значение должно быть равно ожидаемому.\n" \
              f"Фактическое значение = '{actual_value}',\n" \
              f"Ожидаемое значение = '{expected_value}'."
    assert actual_value == expected_value, msg


@check_func
def not_equal(
        actual_value: any,
        expected_value: any,
        msg: str = None,
        stop_on_fail: bool = False,
        bug_link: str = None):
    """
    Проверить, что два значения не равны. \n
    :param actual_value: фактическое значение.
    :param expected_value: ожидаемое значение.
    :param msg: сообщение об ошибке. По умолчанию используется сообщение вида:
     'Ошибка! Фактическое значение должно быть не равно ожидаемому.\n
     Фактическое значение = '{actual_value}',\n
     Ожидаемое значение = '{expected_value}'.'
    :param bug_link: ссылка на баг. По умолчанию = None.
    :param stop_on_fail: параметр, отвечающий за необходимость фейлить тест после первой проваленной проверки.
     По умолчанию = False.
    """
    set_stop_on_fail(stop_on_fail)
    if not msg:
        msg = "\nОшибка! Фактическое значение должно быть не равно ожидаемому.\n" \
              f"Фактическое значение = '{actual_value}',\n" \
              f"Ожидаемое значение = '{expected_value}'."
    assert actual_value != expected_value, msg


@check_func
def is_true(
        result: any,
        msg: str = None,
        stop_on_fail: bool = False,
        bug_link: str = None):
    """
    Проверить, что результат выполнения операции равен True. \n
    :param result: результат выполнения операции.
    :param msg: сообщение об ошибке. По умолчанию = None.
    :param bug_link: ссылка на баг. По умолчанию = None.
    :param stop_on_fail: параметр, отвечающий за необходимость фейлить тест после первой проваленной проверки.
     По умолчанию = False.
    """
    set_stop_on_fail(stop_on_fail)
    if not msg:
        msg = f"\nОшибка! Значение должно быть равно 'True'. Фактическое значение = '{result}'."
    assert bool(result), msg


@check_func
def is_false(
        result: any,
        msg: str = None,
        stop_on_fail: bool = False,
        bug_link: str = None):
    """
    Проверить, что результат выполнения операции равен False. \n
    :param result: результат выполнения операции.
    :param msg: сообщение об ошибке. По умолчанию = None.
    :param bug_link: ссылка на баг. По умолчанию = None.
    :param stop_on_fail: параметр, отвечающий за необходимость фейлить тест после первой проваленной проверки.
     По умолчанию = False.
    """
    set_stop_on_fail(stop_on_fail)
    if not msg:
        msg = f"\nОшибка! Значение должно быть равно 'False'. Фактическое значение = '{result}'."
    assert not bool(result), msg


@check_func
def is_none(
        value: any,
        msg: str = None,
        stop_on_fail: bool = False,
        bug_link: str = None):
    """
    Проверить, что значение равно None. \n
    :param value: проверяемое значение.
    :param msg: сообщение об ошибке. По умолчанию используется сообщение вида:
     'Ошибка! Значение должно быть равно 'None'.\n
      Фактическое значение = '{value}'.'
    :param bug_link: ссылка на баг. По умолчанию = None.
    :param stop_on_fail: параметр, отвечающий за необходимость фейлить тест после первой проваленной проверки.
     По умолчанию = False.
    """
    set_stop_on_fail(stop_on_fail)
    if not msg:
        msg = f"\nОшибка! Значение должно быть равно 'None'. Фактическое значение = '{value}'."
    assert value is None, msg


@check_func
def is_not_none(
        value: any,
        msg: str = None,
        stop_on_fail: bool = False,
        bug_link: str = None):
    """
    Проверить, что значение не равно None. \n
    :param value: проверяемое значение.
    :param msg: сообщение об ошибке. По умолчанию используется сообщение вида:
     'Ошибка! Значение должно быть равно 'None'.\n
      Фактическое значение = '{value}'.'
    :param bug_link: ссылка на баг. По умолчанию = None.
    :param stop_on_fail: параметр, отвечающий за необходимость фейлить тест после первой проваленной проверки.
     По умолчанию = False.
    """
    set_stop_on_fail(stop_on_fail)
    if not msg:
        msg = f"\nОшибка! Значение не должно быть равно 'None'. Фактическое значение = '{value}'."
    assert value is not None, msg


@check_func
def is_in(
        value: any,
        sequence: any,
        msg: str = None,
        stop_on_fail: bool = False,
        bug_link: str = None):
    """
    Проверить, что значение есть в последовательности. \n
    :param value: значение.
    :param sequence: последовательность (строка, список, кортеж, множество или словарь).
    :param msg: сообщение об ошибке. По умолчанию используется сообщение вида:
     'Ошибка! Последовательность '{sequence}' должна содержать значение '{value}'.'
    :param bug_link: ссылка на баг. По умолчанию = None.
    :param stop_on_fail: параметр, отвечающий за необходимость фейлить тест после первой проваленной проверки.
     По умолчанию = False.
    """
    set_stop_on_fail(stop_on_fail)
    if not msg:
        msg = f"\nОшибка! Последовательность '{sequence}' должна содержать значение '{value}'."
    assert value in sequence, msg


@check_func
def is_not_in(
        value: any,
        sequence: any,
        msg: str = None,
        stop_on_fail: bool = False,
        bug_link: str = None):
    """
    Проверить, что значения нет в последовательности. \n
    :param value: значение.
    :param sequence: последовательность (строка, список, кортеж, множество или словарь).
    :param msg: сообщение об ошибке. По умолчанию используется сообщение вида:
     'Ошибка! Последовательность '{sequence}' не должна содержать значение '{value}'.'
    :param bug_link: ссылка на баг. По умолчанию = None.
    :param stop_on_fail: параметр, отвечающий за необходимость фейлить тест после первой проваленной проверки.
     По умолчанию = False.
    """
    set_stop_on_fail(stop_on_fail)
    if not msg:
        msg = f"\nОшибка! Последовательность '{sequence}' не должна содержать значение '{value}'."
    assert value not in sequence, msg


@check_func
def greater(
        first_value: any,
        second_value: any,
        msg: str = None,
        stop_on_fail: bool = False,
        bug_link: str = None):
    """
    Проверить, что первое значение больше второго значения. \n
    :param first_value: первое значение.
    :param second_value: второе значение.
    :param msg: сообщение об ошибке. По умолчанию используется сообщение вида:
     Ошибка! Значение '{first_value}' должно быть больше значения '{second_value}'.
    :param bug_link: ссылка на баг. По умолчанию = None.
    :param stop_on_fail: параметр, отвечающий за необходимость фейлить тест после первой проваленной проверки.
     По умолчанию = False.
    """
    set_stop_on_fail(stop_on_fail)
    if not msg:
        msg = f"\nОшибка! Значение '{first_value}' должно быть больше значения '{second_value}'."
    assert first_value > second_value, msg


@check_func
def greater_equal(
        first_value: any,
        second_value: any,
        msg: str = None,
        stop_on_fail: bool = False,
        bug_link: str = None):
    """
    Проверить, что первое значение больше или равно второму значению. \n
    :param first_value: первое значение.
    :param second_value: второе значение.
    :param msg: сообщение об ошибке. По умолчанию используется сообщение вида:
     Ошибка! Значение '{first_value}' должно быть больше или равно значению '{second_value}'.
    :param bug_link: ссылка на баг. По умолчанию = None.
    :param stop_on_fail: параметр, отвечающий за необходимость фейлить тест после первой проваленной проверки.
     По умолчанию = False.
    """
    set_stop_on_fail(stop_on_fail)
    if not msg:
        msg = f"\nОшибка! Значение '{first_value}' должно быть больше или равно значению '{second_value}'."
    assert first_value >= second_value, msg


@check_func
def less(
        first_value: any,
        second_value: any,
        msg: str = None,
        stop_on_fail: bool = False,
        bug_link: str = None):
    """
    Проверить, что первое значение меньше второго значения. \n
    :param first_value: первое значение.
    :param second_value: второе значение.
    :param msg: сообщение об ошибке. По умолчанию используется сообщение вида:
     Ошибка! Значение '{first_value}' должно быть меньше значения '{second_value}'.
    :param bug_link: ссылка на баг. По умолчанию = None.
    :param stop_on_fail: параметр, отвечающий за необходимость фейлить тест после первой проваленной проверки.
     По умолчанию = False.
    """
    set_stop_on_fail(stop_on_fail)
    if not msg:
        msg = f"\nОшибка! Значение '{first_value}' должно быть меньше значения '{second_value}'."
    assert first_value < second_value, msg


@check_func
def less_equal(
        first_value: any,
        second_value: any,
        msg: str = None,
        stop_on_fail: bool = False,
        bug_link: str = None):
    """
    Проверить, что первое значение меньше или равно второму значению. \n
    :param first_value: первое значение.
    :param second_value: второе значение.
    :param msg: сообщение об ошибке. По умолчанию используется сообщение вида:
     Ошибка! Значение '{first_value}' должно быть меньше или равно значению '{second_value}'.
    :param bug_link: ссылка на баг. По умолчанию = None.
    :param stop_on_fail: параметр, отвечающий за необходимость фейлить тест после первой проваленной проверки.
     По умолчанию = False.
    """
    set_stop_on_fail(stop_on_fail)
    if not msg:
        msg = f"\nОшибка! Значение '{first_value}' должно быть меньше или равно значению '{second_value}'."
    assert first_value <= second_value, msg


@check_func
def check_dict_values(
        actual_data: dict,
        expected_data: dict,
        verified_fields: list = None,
        unverified_fields: list = None,
        msg: str = None,
        stop_on_fail: bool = False,
        bug_link: str = None):
    """
    Проверить, что все значения из словаря с ожидаемыми данными равны значениям из словаря с фактическими данными. \n
    :param actual_data: словарь с фактическими данными.
    :param expected_data: словарь с ожидаемыми данными.
    :param msg: сообщение об ошибке. По умолчанию используется сообщение вида:
     'Ошибка! Фактическое значение должно быть равно ожидаемому.\n
     Фактическое значение = '{actual_value}',\n
     Ожидаемое значение = '{expected_value}'.'
    :param bug_link: ссылка на баг. По умолчанию = None.
    :param stop_on_fail: параметр, отвечающий за необходимость фейлить тест после первой проваленной проверки.
     По умолчанию = False.
    """
    set_stop_on_fail(stop_on_fail)
    verified_keys = expected_data.keys()
    if verified_fields:
        verified_keys = verified_fields
    elif unverified_fields:
        verified_keys -= unverified_fields
    for key in verified_keys:
        if not msg:
            msg = f"\nОшибка! Фактическое значение поля словаря '{key}' не соответствует ожидаемому.\n" \
                  f"Фактическое значение = '{actual_data.get(key)}',\n" \
                  f"Ожидаемое значение = '{expected_data.get(key)}'."
        assert actual_data.get(key) == expected_data.get(key), msg


@check_func
def check_status_code(
        actual_code: int,
        expected_code: int,
        msg: str = None,
        stop_on_fail: bool = False,
        bug_link: str = None):
    """
    Проверить, что фактический статус-код соответстует ожидаемому. \n
    :param actual_code: фактический статус-код.
    :param expected_code: ожидаемый статус-код.
    :param msg: сообщение об ошибке. По умолчанию используется сообщение вида:
     'Ошибка! Фактический статус-код не соответствует ожидаемому.\n
     Фактический статус-код = '{actual_code}',\n
     Ожидаемый статус-код = '{expected_code}'.'
    :param bug_link: ссылка на баг. По умолчанию = None.
    :param stop_on_fail: параметр, отвечающий за необходимость фейлить тест после первой проваленной проверки.
     По умолчанию = False.
    """
    set_stop_on_fail(stop_on_fail)
    if not msg:
        msg = f"Ошибка! Фактический статус-код не соответствует ожидаемому.\n" \
              f"Фактический статус-код = '{actual_code}',\n" \
              f"Ожидаемый статус-код = '{expected_code}'."
    assert actual_code == expected_code, msg


def get_full_context(level):
    (_, filename, line, funcname, contextlist) = inspect.stack()[level][0:5]
    filename = os.path.relpath(filename)
    context = contextlist[0].strip()
    return (filename, line, funcname, context)


def log_failure(msg):
    __tracebackhide__ = True
    level = 3
    pseudo_trace = []
    func = ""
    while "test_" not in func:
        (file, line, func, context) = get_full_context(level)
        if "site-packages" in file:
            break
        line = "{}:{} in {}() -> {}\n".format(file, line, func, context)
        pseudo_trace.append(line)
        level += 1
    pseudo_trace_str = "\n".join(reversed(pseudo_trace))
    entry = "FAILURE: {}\n{}".format(msg if msg else "", pseudo_trace_str)
    _failures.append(entry)


def check_issue(issue_info, exception: AssertionError):
    """
    Проверить актуальность дефектов. \n
    :param issue_info: данные о задаче.
    :param exception: данные об ошибке сравнения.
    """
    unfixed_bug_msg, fixed_bug_msg = '', ''
    if issue_info:
        if issue_info.fields.created is not None:
            status_name = issue_info.fields.status.name
            if status_name != 'Готово':
                unfixed_bug_msg = \
                    f"\nТест падает по дефекту: https://jira.zyfra.com/browse/{issue_info.key},\n" \
                    f"Приоритет задачи: '{issue_info.fields.priority}'!\n" \
                    f"Статус задачи: '{status_name}'!\n"
            elif status_name == 'Готово':
                versions = ', '.join([service.name for service in issue_info.fields.fixVersions])
                fixed_bug_msg = \
                    f"\nВоспроизводится дефект: https://jira.zyfra.com/browse/{issue_info.key},\n" \
                    f"Статус задачи: '{status_name}',\n" \
                    f"Дата решения задачи: '{issue_info.fields.resolutiondate}',\n" \
                    f"Баг исправлен в версиях: '{versions}'!\n"
        else:
            reason = exception.args[0] + f"\nЗадача с номером '{issue_info.key}' не найдена в Jira!"
            log_failure(reason)
            raise exception
        if unfixed_bug_msg:
            testit.addLink(type=testit.LinkType.DEFECT, url=f'https://jira.zyfra.com/browse/{issue_info.key}')
            reason = exception.args[0] + unfixed_bug_msg
            log_failure(reason)
            pytest.xfail(reason=reason)
        elif fixed_bug_msg:
            reason = exception.args[0] + fixed_bug_msg
            log_failure(reason)
    else:
        reason = exception.args[0] + "\nТест падает по дефекту! Мы уже работаем над его исправлением!"
        log_failure(reason)
        pytest.xfail("Тест падает по дефекту! Мы уже работаем над его исправлением!")
