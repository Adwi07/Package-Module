import logging

from .config import LOG_DIR, LOG_FILE


def get_logger():
    """
    Create and return the application logger.
    """
    LOG_DIR.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger("FileOrganizer")
    logger.setLevel(logging.INFO)

    # Avoid adding duplicate handlers if called repeatedly.
    if logger.handlers:
        return logger

    file_handler = logging.FileHandler(
        LOG_FILE,
        encoding="utf-8"
    )

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger