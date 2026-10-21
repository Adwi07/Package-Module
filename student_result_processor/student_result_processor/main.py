"""Command-line entry point for the fault-tolerant result processor."""
import logging

from .exceptions import InvalidStudentCountError, StudentResultError
from .logging_config import configure_logging
from .result_calculation import calculate_result
from .student_operations import SUBJECTS, create_student
from .student_storage import save_student_result, display_all_students

logger = logging.getLogger(__name__)


def read_student_count() -> int:
    """Read a positive number of student records from the user."""
    raw_count = input("How many students do you want to process? ").strip()
    try:
        count = int(raw_count)
    except ValueError as exc:
        raise InvalidStudentCountError("Student count must be a whole number.") from exc
    if count <= 0:
        raise InvalidStudentCountError("Student count must be greater than zero.")
    return count


def print_result(result: dict) -> None:
    """Display one student's calculated result."""
    student = result["student"]
    print("\n" + "-" * 48)
    print(f"Student name : {student.name}")
    print(f"Student ID   : {student.student_id}")
    print("Marks        : " + ", ".join(
        f"{subject}={mark:g}" for subject, mark in zip(SUBJECTS, student.marks)
    ))
    print(f"Total        : {result['total']:.2f}/{result['maximum']}")
    print(f"Percentage   : {result['percentage']:.2f}%")
    print(f"Grade        : {result['grade']}")
    print(f"Status       : {result['status']}")
    print("-" * 48)


def process_one_student(index: int) -> dict | None:
    """Collect, validate, and calculate one record; log and skip bad records."""
    print(f"\nStudent {index}")
    try:
        name = input("Full name: ")
        student_id = input("Student ID: ")
        raw_marks = [input(f"{subject} marks (0–100): ") for subject in SUBJECTS]
        student = create_student(name, student_id, raw_marks)
        result = calculate_result(student)
        print_result(result)
        return result
    except StudentResultError as exc:
        logger.error("Student %s was skipped: %s", index, exc)
        print(f"ERROR: Student {index} was skipped: {exc}")
    except (EOFError, KeyboardInterrupt):
        logger.warning("Input interrupted while processing student %s.", index)
        print("\nInput interrupted. Remaining students will not be requested.")
        raise
    except Exception:
        # Last-resort isolation: unexpected errors do not crash the whole batch.
        logger.exception("Unexpected error while processing student %s.", index)
        print(f"ERROR: Unexpected problem processing student {index}; see the log file.")
    return None


def main() -> None:
    """Run the batch, continuing after individual student-record failures."""
    configure_logging()
    print("=" * 48)
    print("       FAULT-TOLERANT STUDENT RESULT PROCESSOR")
    print("=" * 48)

    try:
        count = read_student_count()
    except InvalidStudentCountError as exc:
        logger.error("Invalid batch size: %s", exc)
        print(f"ERROR: {exc}")
        return

    results = []
    for index in range(1, count + 1):
        try:
            result = process_one_student(index)
            if result is not None:
                results.append(result)
                save_student_result(result)
        except (EOFError, KeyboardInterrupt):
            break
    display_all_students()

    passed = sum(result["status"] == "PASS" for result in results)
    failed = sum(result["status"] == "FAIL" for result in results)
    print("\nBATCH SUMMARY")
    print(f"Records requested : {count}")
    print(f"Results calculated: {len(results)}")
    print(f"Passed            : {passed}")
    print(f"Failed            : {failed}")
    print(f"Skipped due to errors: {count - len(results)}")
    print("Log file: logs/student_result_processor.log")
    logger.info("Batch completed: %s calculated, %s passed, %s failed.", len(results), passed, failed)


if __name__ == "__main__":
    main()
