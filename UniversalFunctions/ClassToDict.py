from collections.abc import Callable
from .Validators.QuantumValidators import qtm_lt_validator


def classes_to_dict(*classes: tuple[type, ...]) -> dict[str, Callable]:
    """
    Takes given classes, extracts the name + function of each class and returns a dictionary
    :param classes:
    :return:
    """
    qtm_lt_validator(classes, tuple[type, ...], "classes")
    dictionary = {}
    for cls in classes:
        dictionary.update({
            name: obj
            for name, obj in vars(cls).items()
            if callable(obj)
        })
    return dictionary