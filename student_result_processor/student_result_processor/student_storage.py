
"""Save and retrieve student results using a CSV file."""

import csv
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
CSV_FILE = DATA_DIR / "students.csv"

FIELDNAMES = [
    "student_id",
    "name",
    "mathematics",
    "physics",
    "chemistry",
    "computer_science",
    "english",
    "total",
    "maximum",
    "percentage",
    "grade",
    "status",
]


def save_student_result(result: dict) -> None:
    """Append one calculated student result to the CSV file."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    student = result["student"]
    file_exists = CSV_FILE.exists()
    file_is_empty = not file_exists or CSV_FILE.stat().st_size == 0

    with CSV_FILE.open("a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)

        if file_is_empty:
            writer.writeheader()

        row = {
            "student_id": student.student_id,
            "name": student.name,
            "mathematics": student.marks[0],
            "physics": student.marks[1],
            "chemistry": student.marks[2],
            "computer_science": student.marks[3],
            "english": student.marks[4],
            "total": result["total"],
            "maximum": result["maximum"],
            "percentage": result["percentage"],
            "grade": result["grade"],
            "status": result["status"],
        }

        writer.writerow(row)


def get_all_students() -> list[dict]:
    """Return all previously saved student records."""
    if not CSV_FILE.exists():
        return []

    with CSV_FILE.open("r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def display_all_students() -> None:
    """Print the saved student records."""
    students = get_all_students()

    if not students:
        print("No saved student records found.")
        return

    for student in students:
        print("-" * 45)
        print(f"Student ID : {student['student_id']}")
        print(f"Name       : {student['name']}")
        print(
            "Marks      : "
            f"Maths={student['mathematics']}, "
            f"Physics={student['physics']}, "
            f"Chemistry={student['chemistry']}, "
            f"CS={student['computer_science']}, "
            f"English={student['english']}"
        )
        print(f"Total      : {student['total']}/{student['maximum']}")
        print(f"Percentage : {student['percentage']}%")
        print(f"Grade      : {student['grade']}")
        print(f"Status     : {student['status']}")
