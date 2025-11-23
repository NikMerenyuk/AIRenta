from pydantic import BaseModel
import random

class Apartment(BaseModel):
    city: str
    rooms: int
    price: float
    area: float

CITIES = ['Москва', "Санкт-Петербург", "Новосибирск", "Екатеринбург", "Казань"]


def generate_random_apartment():
    return Apartment(
        city=random.choice(CITIES),
        rooms=random.randint(1, 5),
        price=round(random.uniform(1_000_000, 30_000_000), 2),
        area=round(random.uniform(20, 200), 2),
    )
