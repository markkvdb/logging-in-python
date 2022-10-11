"""Our super logging app."""

import logging
import os

from loguru import logger
from notifiers.logging import NotificationHandler
from rich.logging import RichHandler

from logging_in_python.lib import print_something

logger.configure(
    handlers=[
        {
            "sink": RichHandler(),
            "format": "<level>{message}</level>",
        }
    ]
)

if os.environ.get("ENV", "prod").lower() == "prod":
    slack_handler = NotificationHandler("slack", defaults={"webhook_url": "<webhook_url>"})
    slack_handler.setLevel(logging.ERROR)
    logger.add(slack_handler)



def main() -> None:
    """Business code."""
    try:
        x = 1 / 0
    except ZeroDivisionError as exc:
        logger.exception("divided by zero")
        raise exc
        
    print_something()
    
if __name__ == "__main__":
    main()
