import os
import pandas as pd
import logging
from src.ingestion.csv_loader import load_csv
from src.ingestion.json_loader import load_json
from src.ingestion.excel_loader import load_excel
from src.validation.schema import Order
from src.database.postgres import save_to_db
from src.storage.parquet_writer import save_to_parquet

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def process_file(file_path: str):
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".csv":
        df = load_csv(file_path)
    elif ext == ".json":
        df = load_json(file_path)
    elif ext in [".xls", ".xlsx"]:
        df = load_excel(file_path)
    else:
        raise ValueError(f"Unsupported file format: {ext}")

    valid_records = []
    for record in df.to_dict(orient="records"):
        try:
            valid_records.append(Order(**record).model_dump())
        except Exception as e:
            logger.warning(f"Invalid record dropped: {record} - Error: {e}")

    clean_df = pd.DataFrame(valid_records)

    if not clean_df.empty:
        save_to_db(clean_df, "orders")
        parquet_path = file_path.replace(ext, ".parquet")
        save_to_parquet(clean_df, parquet_path)
        logger.info("Pipeline completed successfully.")
    else:
        logger.warning("No valid records to process.")
