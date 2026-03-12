import os
import logging
from sqlalchemy import create_engine
import pandas as pd

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


DB_URL = "postgresql://postgres:password@localhost:5433/dataplatform"


def get_engine():
    return create_engine(DB_URL)


def save_to_db(df: pd.DataFrame, table_name: str):
    try:
        engine = get_engine()
        logger.info(f"Saving data to table: {table_name}")
        df.to_sql(table_name, engine, if_exists="append", index=False)
    except Exception as e:
        logger.error(f"Database error: {e}")
        raise
