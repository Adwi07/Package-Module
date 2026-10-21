# Fault-Tolerant Student Result Processor

A modular Python command-line application that collects student details and marks for five subjects, validates the input, calculates totals, percentages, grades, and pass/fail status, and logs problems without allowing one invalid student record to stop the rest of the batch.

## Features

- Collects student name, student ID, and marks in Mathematics, Physics, Chemistry, Computer Science, and English.
- Validates missing student details, non-numeric marks, and marks outside the inclusive 0–100 range.
- Defines custom exceptions for expected input and processing errors.
- Calculates total out of 500, percentage, grade, and pass/fail status.
- A student passes only when **every subject mark is at least 33**.
- Logs events to the console and `logs/student_result_processor.log`.
- Continues to the next student after a bad record and prints a batch summary.
- Includes unit tests using Python's standard `unittest` framework.

## Requirements

- Python 3.10 or newer (uses modern type hints).
- No third-party packages are required.

## Folder structure

```text
student_result_processor/
├── README.md
├── logs/
│   └── student_result_processor.log   # created automatically at runtime
├── student_result_processor/
│   ├── __init__.py
│   ├── exceptions.py
│   ├── logging_config.py
│   ├── main.py
│   ├── result_calculation.py
│   └── student_operations.py
└── tests/
    └── test_result_calculation.py
```

## Run the program

Open a terminal in the project root (the folder containing `README.md`) and run:

```bash
python -m student_result_processor.main
```

Enter the number of students, then provide the name, ID, and five marks for each student. If one student's data is invalid, that record is logged and skipped; the program then proceeds to the next student.

## Run tests

From the project root:

```bash
python -m unittest discover -s tests -v
```

## Calculation rules

- Total = sum of all five marks; maximum = 500.
- Percentage = `(total / 500) * 100`.
- Pass = every subject is at least 33; otherwise the student fails and receives grade `F`.
- For students who pass: `A+` = 90%+, `A` = 80–89.99%, `B` = 70–79.99%, `C` = 60–69.99%, `D` = 50–59.99%, and `E` = below 50%.

These are example grading rules for this assignment; change the thresholds in `result_calculation.py` if your institution uses a different scheme.

## Design overview

1. `main.py` coordinates the command-line flow and isolates each student's processing attempt.
2. `student_operations.py` owns the `Student` data model and validates input.
3. `exceptions.py` defines domain-specific errors that the application can catch intentionally.
4. `result_calculation.py` contains the calculation rules, separate from input/output.
5. `logging_config.py` configures console and file logging in one place.
6. `tests/` checks the key calculations and validation rules.

## Fault tolerance and limitations

Expected validation errors are caught per student, logged, and skipped. A broad final exception handler is included as a last-resort boundary so an unexpected issue in one record does not crash the entire batch; the traceback is written to the log. If input is interrupted with Ctrl+C or end-of-file, the current batch stops gracefully. This is a console-based educational project; it does not persist student records to a database or export results to CSV.
