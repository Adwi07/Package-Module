# Python Packages and Modules

A collection of Python projects demonstrating how to organize code into reusable packages and modules. This repository currently contains two projects: **FileOrganizer** and **Calculator Tools**.

The goal is to practice modular programming, code reusability, exception handling, file operations, and working with Python packages.

## 📁 Repository Structure

```text
Package-Module/
│
├── FileOrganizer/
│   ├── __init__.py
│   ├── main.py
│   ├── file_detection.py
│   ├── file_movement.py
│   ├── logging_config.py
│   └── exception_handling.py
│
├── calculator_tools/
│   ├── __init__.py
│   └── ... (calculator modules)
│
└── README.md
```

*Note: The structure above illustrates the intended organization. The exact module filenames may differ depending on the files present in each folder.*

---

# 1. 📂 File Organizer

## About the Project

File Organizer is a Python application that organizes files in a specified directory according to their file extensions. It separates files into appropriate categories, making folders easier to manage.

### Features

- **File detection:** Identifies file types using their extensions.
- **File movement:** Moves files into category-specific folders.
- **Logging:** Records important operations and errors.
- **Exception handling:** Handles common problems, including missing files, permission errors, and unsupported file types.
- **Duplicate handling:** Helps prevent files with identical names from overwriting each other.

### Supported File Categories

| File extensions | Destination folder |
|---|---|
| `.jpg`, `.jpeg`, `.png`, `.gif` | `Images/` |
| `.txt`, `.log` | `Text/` |
| `.pdf`, `.docx`, `.doc` | `Documents/` |
| `.csv`, `.xlsx`, `.xls` | `Data/` |
| Other extensions | Handled according to the project's configuration |

## Requirements

- Python 3.10 or later recommended.
- No third-party packages are required if the project uses only Python's standard library.

Check your Python installation:

```bash
python --version
```

## How to Run File Organizer

### Step 1: Open the project directory

Open PowerShell or the VS Code terminal and navigate to the directory containing both project folders.

For example:

```powershell
cd D:\Tasks\PackagesANDmodules
```

**Important:** Run the command from the parent directory of `FileOrganizer`, not from inside the `FileOrganizer` folder.

### Step 2: Execute the application

Run the following command:

```powershell
python -m FileOrganizer.main
```

Using `-m` runs `main` as a module within the `FileOrganizer` package, allowing Python to resolve package imports correctly.

### Step 3: Enter the folder path

The application will ask:

```text
=============================================
         PYTHON FILE ORGANIZER
=============================================
Enter the folder path to organize:
```

Enter the full path to the folder you want to organize.

For example:

```text
D:\Tasks\TestFiles
```

Make sure the folder exists and contains test files before running the application.

### Step 4: Check the results

Suppose your input folder initially contains:

```text
TestFiles/
├── photo.jpg
├── notes.txt
├── report.pdf
└── data.csv
```

After successful organization, the expected structure would be:

```text
TestFiles/
├── Images/
│   └── photo.jpg
├── Text/
│   └── notes.txt
├── Documents/
│   └── report.pdf
└── Data/
    └── data.csv
```

The actual destination folders and supported extensions depend on the project's implementation.

## Error Handling

The application is designed to account for common file-operation problems, such as:

- A source directory that does not exist.
- Files that cannot be accessed because of permissions.
- Duplicate filenames in destination folders.
- Unsupported file extensions.
- Errors encountered while moving files.

Always test the organizer on a sample directory first, rather than a folder containing important files.

---

# 2. 🧮 Calculator Tools

## About the Project

The `calculator_tools` package demonstrates how mathematical and statistical functions can be separated into reusable Python modules.

Instead of writing every calculation in one large file, individual functions can be organized into modules and imported wherever they are needed.

### Example Calculations

Depending on the functions implemented in the package, calculator tools can include:

- Mean (average)
- Median
- Mode
- Standard deviation
- Other mathematical or statistical operations

### Example Usage

The following illustrates how statistical functions can be called from Python. The import statement must match the actual module and function names in your package.

```python
from calculator_tools import calculate_mean

numbers = [1, 2, 3, 4, 5]

result = calculate_mean(numbers)

print("Mean:", result)
```

Expected output:

```text
Mean: 3.0
```

If the functions are defined in separate modules, import them from their respective modules instead. For example, if `calculate_mean` is defined in `mean.py`:

```python
from calculator_tools.mean import calculate_mean
```

### How to Run Calculator Tools

1. Open the `Package-Module` directory in VS Code.
2. Expand the `calculator_tools` folder.
3. Locate the file containing the example code or the application's entry point.
4. Run the appropriate Python file or module from the repository's parent directory.

If the package contains a `main.py` entry point, you can run:

```powershell
python -m calculator_tools.main
```

If it contains only reusable functions, import and call those functions from a separate test script.

**Note:** The exact command depends on whether your `calculator_tools` package contains a `main.py`, a test script, or only individual calculation modules.

---

# 3. 🧠 Concepts Demonstrated

These projects provide practical experience with the following Python concepts:

| Concept | What you learn |
|---|---|
| Packages | Group related Python modules into directories |
| Modules | Split code into separate, reusable files |
| Imports | Reuse functions across modules |
| Functions | Write maintainable, reusable logic |
| Exception handling | Handle errors using `try` and `except` |
| File handling | Inspect and move files using Python |
| Logging | Record program operations and errors |
| Command-line execution | Run packages using `python -m` |
| Testing | Validate functionality with different inputs |

---

# 4. 🚀 Getting Started

Clone the repository:

```bash
git clone https://github.com/Adwi07/Package-Module.git
```

Navigate to the project:

```bash
cd Package-Module
```

Run the File Organizer:

```bash
python -m FileOrganizer.main
```

To use Calculator Tools, inspect the `calculator_tools` directory and follow its entry-point or import instructions.

---

# 5. 🎯 Learning Objectives

By working with these projects, you can learn how to:

- Design Python applications using packages and modules.
- Separate responsibilities across multiple files.
- Build reusable functions and import them into other programs.
- Handle errors without unexpectedly terminating an application.
- Work with files and directories programmatically.
- Test applications using different inputs and edge cases.

## Future Improvements

Possible enhancements include adding automated unit tests, supporting more file extensions, generating detailed logs, adding a command-line interface, and improving documentation for each module.

---

**Author:** [Adwi07](https://github.com/Adwi07)

**Repository:** [Package-Module](https://github.com/Adwi07/Package-Module)
