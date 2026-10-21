"""Pure functions for calculating totals, percentages, grades, and status."""
import logging
from typing import Any

from .exceptions import StudentResultError
from .student_operations import Student, SUBJECTS

logger = logging.getLogger(__name__)
PASS_MARK = 33.0


def calculate_result(student: Student) -> dict[str, Any]:
    """Calculate a result. A student passes only if every subject is >= 33."""
    try:
        total = sum(student.marks)
        maximum = len(SUBJECTS) * 100
        percentage = (total / maximum) * 100
    except ZeroDivisionError as exc:
        # Defensive guard: the fixed five-subject configuration should prevent this.
        logger.exception("Could not calculate result for student %s.", student.student_id)
        raise StudentResultError("Cannot calculate percentage with a zero maximum.") from exc

    passed = all(mark >= PASS_MARK for mark in student.marks)
    if not passed:
        grade = "F"
    elif percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "E"

    result = {
        "student": student,
        "total": round(total, 2),
        "maximum": maximum,
        "percentage": round(percentage, 2),
        "grade": grade,
        "status": "PASS" if passed else "FAIL",
    }
    logger.info("Calculated result for student ID %s.", student.student_id)
    return result
