import asyncio
from contextlib import asynccontextmanager
from random import randint
from typing import List

from fastapi import FastAPI

from services.mock_realty_service.models import *


# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     # Load the ML model
#     print("Создание сервиса")
#     yield
#     # Clean up the ML models and release the resources
#     print("Закрытие")

# app = FastAPI(lifespan=lifespan)
app = FastAPI()


# TODO: Разнести эндпоинты и старт по разным директориям

# TODO: router - почитать за них

# TODO router: api/v1
#
# router /apartments
#         router /{id}
#         router /{}
# Middleware
# event startup (lifecycle)

# TODO: сделать разные статус коды
@app.get("/apartments/", response_model=List[Apartment])
async def get_apartments(
        city: str = None,
        min_rooms: int = 1,
        max_rooms: int = 5,
        limit: int = 10,
):
    await asyncio.sleep(randint(2, 7))
    # TODO логику прячем внутрь слой логики. Читать за луковую архитектуру
    apartments = []
    for _ in range(limit):
        # TODO Тут сделали фабрику
        apt = generate_random(Apartment)


        if city and apt.city.lower() != city.lower():
            continue
        if not (min_rooms <= apt.rooms <= max_rooms):
            continue
        apartments.append(apt)

    return apartments[:limit]


def deco(func):
    def wrapper(*args, **kwargs):
        pre_func()
        res = func(*args, **kwargs)
        post_func()
        return res
    return wrapper