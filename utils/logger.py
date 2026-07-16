"""
Logging configuration.
"""

import logging
from pathlib import Path

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "job-agent.log"


def setup_logger():

    logger = logging.getLogger("JobAgent")

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(message)s"
    )

    # Console output
    console = logging.StreamHandler()
    console.setFormatter(formatter)

    # File output
    file = logging.FileHandler(LOG_FILE)
    file.setFormatter(formatter)

    logger.addHandler(console)
    logger.addHandler(file)

    return logger