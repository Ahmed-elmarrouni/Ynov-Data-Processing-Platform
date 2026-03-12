````md
# Ynov Data Processing Platform

This is a data engineering project for my lab. It takes raw data files (like Excel), cleans the data, saves it to a PostgreSQL database, and converts it to Parquet format for fast reading. It also has a web API to show the results.

## Tools Used

- **Language:** Python 3
- **Database:** PostgreSQL (with Docker)
- **Libraries:** Pandas, FastAPI, SQLAlchemy, Pydantic, Pytest

## How to Run the Project

### 1. Start the Database

Make sure Docker is running on your computer. Then, open your terminal and type:

```bash
docker-compose up -d db
```
````

### 2. Run the Data Pipeline

This step will read the `sales_data.xlsx` file, save the good data to the database, and create a `.parquet` file:

```bash
pip install -r requirements.txt
python3 main.py

```

### 3. Start the API

To see the data on the web, start the FastAPI server:

```bash
uvicorn src.api.main:app --reload

```

You can now open these links in your browser:

- **Orders:** [http://127.0.0.1:8000/orders](http://127.0.0.1:8000/orders)
- **Total Revenue:** [http://127.0.0.1:8000/revenue](http://127.0.0.1:8000/revenue)

### 4. Run the Tests

To check if the code works correctly, run the automated tests:

```bash
python3 -m pytest tests/

```

![architecture diagram](<images/architecture diagram.png>)

![Dashboard Overview](<images/Dashboard Overview.png>)

![ders List filtred](<images/Orders List filtred.png>)

![Orders List](<images/Orders List.png>)
