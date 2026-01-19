from pydantic import BaseModel
from datetime import date,datetime

class Product(BaseModel):
    id: str
    name: str
    sku: str
    type: str
    price: float
    description: str
    status: str

class Store(BaseModel):
    id: str
    name: str
    opened_at: datetime
    tax_rate: float
    status: str