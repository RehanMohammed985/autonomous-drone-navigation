import logging
import os

def setup_logger(log_dir="logs", log_file="training.log"):
    os.makedirs(log_dir, exist_ok=True)
    logger = logging.getLogger("drone_nav")
    logger.setLevel(logging.INFO)

    # File handler
    fh = logging.FileHandler(f"{log_dir}/{log_file}")
    fh.setLevel(logging.INFO)

    # Console handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    # Formatter
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # Add handlers
    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger
