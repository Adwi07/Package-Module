"""Input validation and student data collection."""
from dataclasses import dataclass
import logging
from typing import Sequence

from .exceptions import InvalidMarksError, MissingStudentInfoError

logger = logging.getLogger(__name__)
SUBJECTS = ("Mathematics", "Physics", "Chemistry", "Computer Science", "English")


@dataclass(frozen=True)
class Student:
    """Validated student information and five subject marks."""
    name: str
    student_id: str
    marks: tuple[float, ...]


def validate_student_info(name: str, student_id: str) -> tuple[str, str]:
    """Strip and validate the required identity fields."""
    clean_name = name.strip()
    clean_id = student_id.strip()
    if not clean_name or not clean_id:
        raise MissingStudentInfoError("Student name and student ID are required.")
    return clean_name, clean_id


def validate_marks(raw_marks: Sequence[str]) -> tuple[float, ...]:
    """Convert five mark inputs to numbers and enforce the 0–100 range."""
    if len(raw_marks) != len(SUBJECTS):
        raise InvalidMarksError(f"Exactly {len(SUBJECTS)} subject marks are required.")

    parsed_marks = []
    for subject, raw_mark in zip(SUBJECTS, raw_marks):
        try:
            mark = float(raw_mark)
        except (TypeError, ValueError) as exc:
            raise InvalidMarksError(
                f"{subject} mark must be numeric; received {raw_mark!r}."
            ) from exc

        if not 0 <= mark <= 100:
            raise InvalidMarksError(
                f"{subject} mark must be between 0 and 100; received {mark}."
            )
        parsed_marks.append(mark)

    return tuple(parsed_marks)


def create_student(name: str, student_id: str, raw_marks: Sequence[str]) -> Student:
    """Validate raw values and return a Student object."""
    clean_name, clean_id = validate_student_info(name, student_id)
    marks = validate_marks(raw_marks)
    student = Student(name=clean_name, student_id=clean_id, marks=marks)
    logger.info("Validated student record for ID %s.", clean_id)
    return student
