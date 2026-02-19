import logging
import os

def setup_logger():
    if not os.path.exists("logs"):
        os.makedirs("logs")

    logging.basicConfig(
        filename="logs/ai_system.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    return logging.getLogger()
