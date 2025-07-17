import logging 
import os 
from datetime import datetime

LOGS_DIR = "logs"

# Create the logs directory if it doesn't exist
os.makedirs(LOGS_DIR, exist_ok=True) 

# Create a unique log file name (timestamped)
log_file = os.path.join(LOGS_DIR, f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")

# Set up basic logger configuration
logging.basicConfig(
    filename=log_file,
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Get logger object
def get_logger(name: str) -> logging.Logger:
    """
    Returns a logger object with the specified name.

    Args:
        name (str): The name of the logger.

    Returns:
        logging.Logger: A logger object.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger
