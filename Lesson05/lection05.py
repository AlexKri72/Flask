import logging
from fastapi import FastAPI

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

app = FastAPI()


@app.put('/items/{item_id}')
async def update_item(item_id: int, item: Item):
    logger.info(f'отработал PUT запрос для item id = {item_id}')
    return {'item_id': item_id, 'item': item}
