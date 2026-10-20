from pathlib import Path

from .detector import detect_file_category
from .mover import move_file
from .logger_setup import get_logger

from .exceptions import (
    UnsupportedFileError,
    SourceFolderNotFoundError,
    DestinationFolderError,
    FileMoveError,
)


def organize_folder(source_folder):
    """
    Organize files in a folder according to their extensions.

    Returns a dictionary containing successful, failed,
    and skipped operation counts.
    """
    logger = get_logger()

    source_folder = Path(source_folder).resolve()

    summary = {
        "successful": 0,
        "failed": 0,
        "skipped": 0,
    }

    # Step 1: Validate the source folder.
    if not source_folder.exists():
        error = SourceFolderNotFoundError(
            f"Source folder does not exist: {source_folder}"
        )
        logger.error("FAILED | %s", error)
        raise error

    if not source_folder.is_dir():
        error = NotADirectoryError(
            f"Source path is not a directory: {source_folder}"
        )
        logger.error("FAILED | %s", error)
        raise error

    # Step 2: Read the folder contents.
    try:
        entries = list(source_folder.iterdir())

    except OSError as error:
        logger.exception(
            "FAILED | Could not read source folder: %s",
            source_folder,
        )
        raise

    # Step 3: Process each entry independently.
    for file_path in entries:

        # Do not process folders as files.
        if file_path.is_dir():
            summary["skipped"] += 1
            continue

        try:
            # Detect the category from the extension.
            category = detect_file_category(file_path)

            # Construct the destination folder path.
            destination_folder = source_folder / category

            # Move the file.
            destination_path = move_file(
                file_path,
                destination_folder,
            )

            # Record success.
            logger.info(
                "SUCCESS | %s moved to %s",
                file_path.name,
                destination_path,
            )

            summary["successful"] += 1

        except UnsupportedFileError as error:
            logger.error(
                "FAILED | Unsupported file | %s | %s",
                file_path.name,
                error,
            )
            summary["failed"] += 1

        except FileNotFoundError as error:
            logger.error(
                "FAILED | File not found | %s | %s",
                file_path.name,
                error,
            )
            summary["failed"] += 1

        except PermissionError as error:
            logger.error(
                "FAILED | Permission denied | %s | %s",
                file_path.name,
                error,
            )
            summary["failed"] += 1

        except (
            DestinationFolderError,
            FileMoveError,
            OSError,
        ) as error:
            logger.error(
                "FAILED | File operation | %s | %s",
                file_path.name,
                error,
            )
            summary["failed"] += 1

        except Exception as error:
            logger.exception(
                "FAILED | Unexpected error | %s",
                file_path.name,
            )
            summary["failed"] += 1

    return summary
