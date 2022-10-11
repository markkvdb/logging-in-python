"""Our super logging app."""

import os

from loguru import logger
from notifiers.logging import NotificationHandler
from rich.logging import RichHandler

from logging_in_python.lib import print_something

logger.remove()
logger.add(RichHandler(), format="<level>{message}</level>")

if os.environ.get("ENV", "prod").lower() == "prod":
    logger.add(
        NotificationHandler("slack", defaults={"webhook_url": "<webhook_url"}),
        level="ERROR",
        format="{level}: {message}",
    )


def main() -> None:
    """Business code."""
    try:
        x = 1 / 0
    except ZeroDivisionError as exc:
        logger.exception("divided by zero")

    print_something()


if __name__ == "__main__":
    main()
