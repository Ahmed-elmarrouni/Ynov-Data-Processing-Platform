from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from src.database.postgres import get_engine

app = FastAPI()

# This allows your HTML file to fetch data from this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/revenue")
def get_total_revenue():
    try:
        with get_engine().connect() as conn:
            query = text("SELECT SUM(price * quantity) FROM orders")
            result = conn.execute(query).scalar()
        return {"total_revenue": float(result) if result else 0.0}
    except Exception as e:
        return {"error": str(e)}


@app.get("/revenue/country")
def get_revenue_by_country():
    try:
        with get_engine().connect() as conn:
            query = text(
                "SELECT country, SUM(price * quantity) as revenue FROM orders GROUP BY country ORDER BY revenue DESC LIMIT 5"
            )
            result = conn.execute(query).mappings().all()
        return {"revenue_by_country": [dict(row) for row in result]}
    except Exception as e:
        return {"error": str(e)}


@app.get("/top-products")
def get_top_products():
    try:
        with get_engine().connect() as conn:
            query = text(
                "SELECT product, SUM(quantity) as total_sold FROM orders GROUP BY product ORDER BY total_sold DESC LIMIT 5"
            )
            result = conn.execute(query).mappings().all()
        return {"top_products": [dict(row) for row in result]}
    except Exception as e:
        return {"error": str(e)}


@app.get("/orders")
def get_orders():
    try:
        with get_engine().connect() as conn:
            query = text(
                "SELECT product, quantity, price, country FROM orders LIMIT 200"
            )
            result = conn.execute(query).mappings().all()
        return {"orders": [dict(row) for row in result]}
    except Exception as e:
        return {"error": str(e)}
