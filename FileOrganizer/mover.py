import shutil
from pathlib import Path

from .exceptions import (
    DuplicateFileError,
    DestinationFolderError,
    FileMoveError,
)


def get_unique_destination(destination_path):
    """
    Return a destination path that does not already exist.

    Example:
        photo.jpg
        photo_1.jpg
        photo_2.jpg
    """
    destination_path = Path(destination_path)

    if not destination_path.exists():
        return destination_path

    if destination_path.exists() and destination_path.is_dir():
        raise DestinationFolderError(
            f"Destination path is a directory: {destination_path}"
        )

    stem = destination_path.stem
    suffix = destination_path.suffix
    parent = destination_path.parent

    counter = 1

    while True:
        new_path = parent / f"{stem}_{counter}{suffix}"

        if not new_path.exists():
            return new_path

        counter += 1


def move_file(source_path, destination_folder):
    """
    Move a file into the specified destination folder.

    Returns:
        The final path of the moved file.
    """
    source_path = Path(source_path)
    destination_folder = Path(destination_folder)

    if not source_path.exists():
        raise FileNotFoundError(
            f"Source file does not exist: {source_path}"
        )

    if not source_path.is_file():
        raise ValueError(
            f"Source path is not a file: {source_path}"
        )

    try:
        destination_folder.mkdir(
            parents=True,
            exist_ok=True
        )

        destination_path = (
            destination_folder / source_path.name
        )

        destination_path = get_unique_destination(
            destination_path
        )

        shutil.move(
            str(source_path),
            str(destination_path)
        )

        return destination_path

    except PermissionError:
        raise

    except OSError as error:
        raise FileMoveError(
            f"Could not move {source_path.name}: {error}"
        ) from error

    