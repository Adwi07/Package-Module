from pathlib import Path
#pathlib is 

from .config import FILE_CATEGORIES
from .exceptions import UnsupportedFileError


def detect_file_category(file_path):
    """
    Determine the category of a file from its extension.

    Args:
        file_path: Path to the file.

    Returns:
        The destination category as a string.

    Raises:
        UnsupportedFileError: If the extension is unsupported.
    """
    file_path = Path(file_path) #file_path = Path(file_path)does 

    extension = file_path.suffix.lower()

    if not extension:
        raise UnsupportedFileError(
            f"File has no extension: {file_path.name}"
        )

    category = FILE_CATEGORIES.get(extension)

    if category is None:
        raise UnsupportedFileError(
            f"Unsupported extension: {extension}"
        )

    return category