import uuid

def uid():
    return str(uuid.uuid4())

def total_price(price: float, quantity: int, tax_rate: float) -> float:
    if quantity < 0:
        raise ValueError("Quantity cannot be negative")
    subtotal = price * quantity
    total = subtotal * tax_rate
    return total


