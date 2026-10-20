from .organizer import organize_folder
from .logger_setup import get_logger


def main():
    logger = get_logger()

    print("=" * 45)
    print("         PYTHON FILE ORGANIZER")
    print("=" * 45)

    source_folder = input(
        "Enter the folder path to organize: "
    ).strip().strip('"')

    try:
        summary = organize_folder(source_folder)

        print("\nOrganization completed!")
        print("-" * 30)
        print(f"Successful: {summary['successful']}")
        print(f"Failed:     {summary['failed']}")
        print(f"Skipped:    {summary['skipped']}")

        logger.info(
            "RUN SUMMARY | Successful=%d | Failed=%d | Skipped=%d",
            summary["successful"],
            summary["failed"],
            summary["skipped"],
        )

    except Exception as error:
        logger.error("RUN FAILED | %s", error)

        print(f"\nCould not organize the folder: {error}")
        print("Check the log file for details.")


if __name__ == "__main__":
    main()
