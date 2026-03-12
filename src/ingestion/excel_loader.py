import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def load_excel(file_path: str) -> pd.DataFrame:
    try:
        logger.info(f"Processing Excel file: {file_path}")
        df = pd.read_excel(file_path)
        return df
    except Exception as e:
        logger.error(f"Error loading Excel {file_path}: {e}")
        raise
