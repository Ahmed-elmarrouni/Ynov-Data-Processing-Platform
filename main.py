import os
from src.pipeline.processor import process_file

if __name__ == "__main__":
    file_to_process = "datasets/sales_data.xlsx"

    if os.path.exists(file_to_process):
        print(f"Starting pipeline for {file_to_process}...")
        process_file(file_to_process)
    else:
        print(f"Error: Could not find {file_to_process}")
