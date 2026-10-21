"""Unit tests for result calculations and validation."""
import unittest

from student_result_processor.exceptions import InvalidMarksError, MissingStudentInfoError
from student_result_processor.result_calculation import calculate_result
from student_result_processor.student_operations import create_student


class StudentResultTests(unittest.TestCase):
    def test_calculates_percentage_and_grade(self):
        student = create_student("Asha Rao", "S101", ["90", "80", "70", "60", "50"])
        result = calculate_result(student)
        self.assertEqual(result["total"], 350)
        self.assertEqual(result["percentage"], 70)
        self.assertEqual(result["grade"], "B")
        self.assertEqual(result["status"], "PASS")

    def test_fails_if_any_subject_is_below_pass_mark(self):
        student = create_student("Ravi Das", "S102", ["90", "90", "20", "90", "90"])
        self.assertEqual(calculate_result(student)["status"], "FAIL")
        self.assertEqual(calculate_result(student)["grade"], "F")

    def test_rejects_non_numeric_marks(self):
        with self.assertRaises(InvalidMarksError):
            create_student("Asha Rao", "S101", ["90", "abc", "70", "60", "50"])

    def test_rejects_out_of_range_marks(self):
        with self.assertRaises(InvalidMarksError):
            create_student("Asha Rao", "S101", ["90", "101", "70", "60", "50"])

    def test_rejects_missing_student_info(self):
        with self.assertRaises(MissingStudentInfoError):
            create_student("  ", "S101", ["90", "80", "70", "60", "50"])


if __name__ == "__main__":
    unittest.main()
