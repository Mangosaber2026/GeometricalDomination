from .FctInputValidators import ctm_validate
from ..TypingVariables import Real

class ValidationParent:
    def __init__(self, expected: Real):
        ctm_validate(expected, Real)
        self.expected = expected

class Positive:
    """Makes sure the entered value is positive"""
    def __call__(self, value: Real) -> None:
        """Validates the entered value, expected to be positive"""
        ctm_validate(value, Real)
        if value < 0:
            raise ValueError(f"Entered value is expected to be greater than 0!")

class LessThan(ValidationParent):
    """Makes sure the entered value is less than expected value"""
    def __call__(self, value: Real) -> bool:
        """Validates the entered value, expected to be less than expected value"""
        ctm_validate(value, Real)
        if value >= self.expected:
            raise ValueError(f"Entered value is expected to be less than or equal to {self.expected!r}!")
        return True

class GreaterThan(ValidationParent):
    """Makes sure the entered value is greater than expected value"""
    def __call__(self, value: Real) -> None:
        """Validates the entered value, expected to be greater than expected value"""
        ctm_validate(value, Real)
        if self.expected >= value:
            raise ValueError(f"Entered value is expected to be greater than or equal to {self.expected!r}!")
