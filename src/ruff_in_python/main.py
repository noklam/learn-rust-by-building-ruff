from pathlib import Path
import typer
import logging
from rich.logging import RichHandler
from ruff_in_python.check import check_ast
from ruff_in_python.parser import parse_file
from rich import print

logger = logging.getLogger()

logging.basicConfig(
    level="NOTSET",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True)],
)


def set_up_logging():
    logger.info("Dummy: set up logging")


def run_once(filepath: str | Path = None):
    filepath = Path(filepath)
    logger.info("run once")
    logger.info(f"Checking {filepath}")
    python_ast = parse_file((filepath))
    errors = check_ast(filepath, python_ast)
    if errors:
        logger.info(f"Found {len(errors)} errors")
    for error in errors:
        logger.warning(error.richify())

    logger.info(f"Finished Checking {filepath}")


app = typer.Typer()


@app.command()
def main(filepath: str):
    if not filepath:
        filepath = "tests/bar.py"
    logger.info(f"flie path: {filepath}")
    set_up_logging()
    run_once(filepath)


if __name__ == "__main__":
    app()
