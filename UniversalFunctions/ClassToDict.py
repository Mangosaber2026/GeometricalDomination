from typing import Callable


def class_to_dict(cls) -> dict[str, Callable]:
    return {
        name: obj
        for name, obj in vars(cls).items()
        if callable(obj)
    }

def classes_to_dict(*classes: type) -> dict[str, Callable]:
    dictionary = {}
    for cls in classes:
        dictionary.update(class_to_dict(cls))
    return dictionary