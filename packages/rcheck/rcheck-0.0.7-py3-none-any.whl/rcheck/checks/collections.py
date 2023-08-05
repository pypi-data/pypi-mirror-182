from typing import Optional

from rcheck.checks.basic_types import _assert_simple_type_fail_message
from rcheck.checks.shared import InvalidRuntype, _isinstance, type_name
from collections.abc import Sequence

#
# list
#
def _print_list_index(val, index):
    val_repr = repr(val)

    if len(val_repr) > 100:
        start_idx = index - 1 if index > 0 else 0
        end = index + 2
        
        print_repr = repr(val[start_idx:end])[1:-1]
        print_repr = f"[ ..., {print_repr}, ... ]"

        pre_spaces = " " * 6

    else:
        start_idx = 0
        print_repr = val_repr
        pre_spaces = ""

    spaces = pre_spaces + " " * (len(repr(val[start_idx:(index + 1)])) - 2)    
    cursor = spaces + "↑"   
    cursor += "\n" + spaces + f"| got type {type_name(type(val[index]))} at index {index}"

    return print_repr + "\n" + cursor

def _assert_list_type_fail_message(
    expected_type_str: str,
    val: object,
    name: str,
    failure_index: int,
    message: Optional[str] = None,
    list_name = "list"
):
    return InvalidRuntype(
        f"Expected items of the {list_name} {name} to be of type {expected_type_str}. \n\n"
        + _print_list_index(val, failure_index)
        + (f"\n\n{message}" if message is not None else "")
    )


def _is_iterable_of(iterable, sub_type):
    for idx, item in enumerate(iterable):
        if not _isinstance(item, sub_type):
            return False, idx

    return True, -1


def is_list(val: object, of: Optional[type] = None):
    if not _isinstance(val, list):
        return False

    return True if of is None else _is_iterable_of(val, of)[0]


def assert_list(
    val: object,
    name: str,
    message: Optional[str] = None,
    *,
    of: Optional[type] = None,
):
    if not _isinstance(val, list):
        raise _assert_simple_type_fail_message("list", val, name, message)

    if of is None:
        return

    items_pass_check, failed_idx = _is_iterable_of(val, of)
    if not items_pass_check:
        raise _assert_list_type_fail_message(
            type_name(of), val, name, failed_idx, message
        )


def _is_iterable_of_opt(iterable, sub_type):
    for idx, item in enumerate(iterable):
        if item is not None and not _isinstance(item, sub_type):
            return False, idx

    return True, -1


def is_list_of_opt(val: object, of: type):
    if not _isinstance(val, list):
        return False

    return _is_iterable_of_opt(val, of)[0]


def assert_list_of_opt(
    val: object,
    of: type,
    name: str,
    message: Optional[str] = None,
):
    if not _isinstance(val, list):
        raise _assert_simple_type_fail_message("list", val, name, message)

    items_pass_check, failed_idx = _is_iterable_of_opt(val, of)
    if not items_pass_check:
        raise _assert_list_type_fail_message(
            type_name(of), val, name, failed_idx, message
        )


def is_opt_list(val: object, of: Optional[type] = None):
    return val is None or is_list(val, of)


def assert_opt_list(
    val: object,
    name: str,
    message: Optional[str] = None,
    *,
    of: Optional[type] = None,
):
    if val is None:
        return

    if not _isinstance(val, list):
        raise _assert_simple_type_fail_message("list", val, name, message)

    if of is None:
        return

    items_pass_check, failed_idx = _is_iterable_of(val, of)
    if not items_pass_check:
        raise _assert_list_type_fail_message(
            type_name(of), val, name, failed_idx, message, list_name="optional list"
        )


#
# dict
#

def _assert_dict_type_fail_message(
    expected_type_str: str,
    val: object,
    name: str,
    failure_index: int,
    message: Optional[str] = None,
    dict_name = "dict"
):
    return InvalidRuntype(
        f"Expected items of the {list_name} {name} to be of type {expected_type_str}. \n\n"
        # + _print_list_index(val, failure_index)
        + (f"\n\n{message}" if message is not None else "")
    )


def assert_dict(
    val: object,
    name: str,
    message: Optional[str] = None,
    *,
    key_of: Optional[type] = None,
    val_of: Optional[type] = None,
):
    if not _isinstance(val, dict):
        raise _assert_simple_type_fail_message("dict", val, name, message)

    if key_of is not None:
        items_pass_check, failed_idx = _is_iterable_of(val.keys(), key_of)
        if not items_pass_check:
            raise _assert_list_type_fail_message(
                type_name(key_of), val, name, failed_idx, message
            )

    if val_of is not None:
        items_pass_check, failed_idx = _is_iterable_of(val.values(), val_of)
        if not items_pass_check:
            raise _assert_list_type_fail_message(
                type_name(val_of), val, name, failed_idx, message
            )

#
# sequences
#
def assert_sequence(
    val: object,
    name: str,
    message: Optional[str] = None,
    *,
    of: Optional[type] = None,
):
    if not _isinstance(val, Sequence):
        raise _assert_simple_type_fail_message("Sequence", val, name, message)

    if of is None:
        return

    items_pass_check, failed_idx = _is_iterable_of(val, of)
    if not items_pass_check:
        raise _assert_list_type_fail_message(
            type_name(of), val, name, failed_idx, message
        )
        