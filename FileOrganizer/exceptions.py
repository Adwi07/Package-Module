class UnsupportedFileError(Exception):
    """Raised when a file extension is not supported."""
    pass


class SourceFolderNotFoundError(Exception):
    """Raised when the source folder does not exist."""
    pass


class DestinationFolderError(Exception):
    """Raised when a destination folder cannot be accessed."""
    pass


class DuplicateFileError(Exception):
    """Raised when a destination filename already exists."""
    pass

class FileMoveError(Exception):
    """Raised when a file cannot be moved to the destination folder."""
    pass