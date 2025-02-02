import logging
from rich.logging import RichHandler

logger = logging.getLogger()

logging.basicConfig(
    level="NOTSET",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True)],
)


def main(filepath: str = None):
    if not filepath:
        filepath = "tests/bar.py"
    logger.info(f"flie path: {filepath}")
    set_up_logging()
    run_once(filepath)


def set_up_logging():
    logger.info("dummy: set up logging")


def run_once(filepath: str = None):
    logger.info("run once")
    logger.info("Identified files to lint in")
    logger.info("Checked files in ")
    logger.info("Found TODO errors")
    errors = []
    for error in errors:
        logger.warning(error)


if __name__ == "__main__":
    main("dummy")
