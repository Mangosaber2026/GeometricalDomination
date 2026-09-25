from collections.abc import Callable
from .FctInputValidators import validate


def classes_to_dict(*classes: type) -> dict[str, Callable]:
    """
    Takes given classes, extracts the name + function of each class and returns a dictionary
    :param classes:
    :return:
    """
    dictionary = {}
    for cls in classes:
        validate(cls, type, "class")

        dictionary.update({
            name: obj
            for name, obj in vars(cls).items()
            if callable(obj)
        })
    return dictionary