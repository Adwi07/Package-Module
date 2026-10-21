"""Custom exceptions used by the student result processor."""

class StudentResultError(Exception):
    """Base class for expected student-result processing errors."""


class MissingStudentInfoError(StudentResultError):
    """Raised when required student information is missing."""


class InvalidMarksError(StudentResultError):
    """Raised when marks are non-numeric or outside the allowed range."""


class InvalidStudentCountError(StudentResultError):
    """Raised when the number of students is invalid."""
