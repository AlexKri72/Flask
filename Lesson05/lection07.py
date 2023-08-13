from typing import Optional
from pydantic import BaseModel
import logging
from fastapi import FastAPI

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.get('/')
async def read_root():
    logger.info('отработал GET запрос')
    return {'hello': 'world'}


@app.put('/items/{item_id}')
async def update_item(item_id: int, item: Item):
    logger.info(f'отработал PUT запрос для item id = {item_id}')
    return {'item_id': item_id, 'item': item}


@app.delete('/items/{item_id}')
async def delete_item(item_id: int):
    logger.info(f'отработал DELETE запрос для item id = {item_id}')
    return {'item_id': item_id}

# POST запрос:
# curl -X 'POST' 'http://127.0.0.1:8000/items/' -H 'accept:
# application/json' -H 'Content-Type: application/json' -d
# '{"name": "BestSale", "description": "The best of the best",
# "price": 9.99, "tax": 0.99}'

# PUT запрос:
# curl -X 'PUT' 'http://127.0.0.1:8000/items/42' -H 'accept:
# application/json' -H 'Content-Type: application/json' -d
# '{"name": "NewName", "description": "New description of the
# object", "price": 77.7, "tax": 10.01}'
# 12

# DELETE запрос:
# curl -X 'DELETE' 'http://127.0.0.1:8000/items/13' -H 'accept:
# application/json'