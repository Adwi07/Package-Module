from pathlib import Path

# The directory where this Python file is located.
BASE_DIR = Path(__file__).resolve().parent

# Log file location.
LOG_DIR = BASE_DIR / "logs"
LOG_FILE = LOG_DIR / "file_organizer.log"

# File extensions mapped to destination folder names.
FILE_CATEGORIES = {
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".webp": "Images",

    ".txt": "Text",
    ".md": "Text",

    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",

    ".csv": "Data",
    ".xlsx": "Data",
    ".json": "Data",

    ".py": "Code",
    ".js": "Code",
    ".html": "Code",
    ".css": "Code",

    ".mp3": "Audio",
    ".wav": "Audio",

    ".mp4": "Videos",
    ".mkv": "Videos",

    ".zip": "Archives",
    ".rar": "Archives",
}

#this above code working is to define the base directory, log file location, and categorize files based on their extensions.
# The FILE_CATEGORIES dictionary maps file extensions to their respective folder names, which can be used to organize files into appropriate directories.
