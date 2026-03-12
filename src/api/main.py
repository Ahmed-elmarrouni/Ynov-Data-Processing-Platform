from fastapi import FastAPI
from sqlalchemy import text
from src.database.postgres import get_engine

app = FastAPI()


@app.get("/revenue")
def get_total_revenue():
    try:
        with get_engine().connect() as conn:
            query = text("SELECT SUM(price * quantity) FROM orders")
            result = conn.execute(query).scalar()
        return {"total_revenue": float(result) if result else 0.0}
    except Exception as e:
        return {"error": str(e)}


@app.get("/orders")
def get_orders():
    try:
        with get_engine().connect() as conn:
            query = text(
                "SELECT product, quantity, price, country FROM orders LIMIT 10"
            )
            result = conn.execute(query).mappings().all()
        return {"orders": [dict(row) for row in result]}
    except Exception as e:
        return {"error": str(e)}
