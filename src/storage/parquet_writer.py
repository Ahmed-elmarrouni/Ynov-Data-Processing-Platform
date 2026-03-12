import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def save_to_parquet(df: pd.DataFrame, file_path: str):
    try:
        logger.info(f"Converting dataset to Parquet: {file_path}")
        df.to_parquet(file_path, engine="fastparquet")
    except Exception as e:
        logger.error(f"Error saving Parquet file {file_path}: {e}")
        raise
