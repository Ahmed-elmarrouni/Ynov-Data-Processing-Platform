from pydantic import BaseModel, Field, field_validator

ALLOWED_COUNTRIES = ["USA", "UK", "France", "Germany", "Canada"]


class Order(BaseModel):
    product: str = Field(..., min_length=1)
    quantity: int = Field(..., gt=0)
    price: float = Field(..., gt=0.0)
    country: str

    # @field_validator("country")
    # @classmethod
    # def check_country(cls, v: str) -> str:
    #     if v not in ALLOWED_COUNTRIES:
    #         raise ValueError(f"Country must be in {ALLOWED_COUNTRIES}")
    #     return v
