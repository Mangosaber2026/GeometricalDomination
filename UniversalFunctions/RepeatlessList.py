from typing import Any


def repeatless_list(old_list: list[Any], new_list: list[Any]) -> list[Any]:
    """
    Takes the 1st list and adds the items to the 2nd list, with no repetitions in the 2nd list
    :param old_list: 1st list
    :param new_list: 2nd list
    :return: 2nd list
    """
    for item in old_list:
        if item not in new_list:
            new_list.append(item)
    return new_list

def repeatless_list2(old_list: list[Any]) -> list[Any]:
    """
    Takes the items from a list and adds its items to a new made list, with no repetitions in the new list
    :param old_list: 1st list
    :return: 2nd list
    """
    new_list: list[Any] = []
    for item in old_list:
        if item not in new_list:
            new_list.append(item)
    return new_list