import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def load_csv(file_path: str) -> pd.DataFrame:
    try:
        logger.info(f"Processing CSV file: {file_path}")
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        logger.error(f"Error loading CSV {file_path}: {e}")
        raise
