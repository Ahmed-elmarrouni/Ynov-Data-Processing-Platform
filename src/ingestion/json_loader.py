import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def load_json(file_path: str) -> pd.DataFrame:
    try:
        logger.info(f"Processing JSON file: {file_path}")
        df = pd.read_json(file_path)
        return df
    except Exception as e:
        logger.error(f"Error loading JSON {file_path}: {e}")
        raise
