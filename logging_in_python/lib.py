"""Our library."""

from loguru import logger


def print_something() -> None:
    """Print something."""
    logger.info("hello")
