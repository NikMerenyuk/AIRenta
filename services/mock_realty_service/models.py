from pydantic import BaseModel
import random

class Apartment(BaseModel):
    city: str
    rooms: int
    price: float
    area: float

    @classmethod
    def generate_random(cls) -> 'Apartment':
        return cls(
            city=random.choice(CITIES),
            rooms=random.randint(1, 5),
            price=round(random.uniform(1_000_000, 30_000_000), 2),
            area=round(random.uniform(20, 200), 2),
        )

CITIES = ['Москва', "Санкт-Петербург", "Новосибирск", "Екатеринбург", "Казань"]

def generate_random(instance):
    return instance.generate_random()

