import logging
from fastapi import FastAPI

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

app = FastAPI()


@app.delete('/items/{item_id}')
async def delete_item(item_id: int):
    logger.info(f'отработал DELETE запрос для item id = {item_id}')
    return {'item_id': item_id}
