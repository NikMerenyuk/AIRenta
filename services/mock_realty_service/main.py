import asyncio
from random import randint
from typing import List

from fastapi import FastAPI

from services.mock_realty_service.models import *

app = FastAPI()

@app.get("/apartments/", response_model=List[Apartment])
async def get_apartments(
        city: str = None,
        min_rooms: int = 1,
        max_rooms: int = 5,
        limit: int = 10,
):
    await asyncio.sleep(randint(2,7))

    apartments = []
    for _ in range(limit):
        apt = generate_random_apartment()
        if city and apt.city.lower() != city.lower():
            continue
        if not (min_rooms <= apt.rooms <= max_rooms):
            continue
        apartments.append(apt)

    return apartments[:limit]
