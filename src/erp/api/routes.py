from schemas import FuelData
import json
from erp.core.calculations import fuel_filled

# Example usage
date = "2023-10-01"
fuel_price = 3.5
amount = 50.0
total_distance_covered = 400.0
ff = fuel_filled(amount, fuel_price)
full_tank_flag = True

k = FuelData(
    date= date,
    fuel_price=fuel_price,
    amount=amount,
    total_distance_covered=total_distance_covered,
    fuel_filled=ff,
    full_tank_flag=full_tank_flag
)

print(k.json())