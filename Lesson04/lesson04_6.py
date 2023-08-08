# Создать программу, которая будет производить подсчет количества слов в каждом файле в указанной директории и выводить результаты в консоль.
# используйте асинхронный подход.

import asyncio
from  pathlib import Path

async def get_file_length(file_name):
    with open(file_name,'r',encoding='utf-8') as f:
        contens=f.read()
        print(f'{f.name} >>> {len(contens)} words')

if __name__=='__main__':
    dir_path=Path('.')
    file=[file_path for file_path in dir_path.iterdir() if file_path.is_file()]
    tasks=[]
    for i in file:
        task = asyncio.ensure_future(get_file_length(i))
        tasks.append(task)
loop=asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
