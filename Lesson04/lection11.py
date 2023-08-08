import  asyncio
from pathlib import Path

async def process_file(file_path):
    with open(file_path,'r',encoding='utf-8') as f:
        contens= f.read()
        print(f'{f.name} содержит  <<< {contens[:13]} ...>>>')

async def main():
    #dir_path=Path('path/to/directory')
    dir_path=Path('.')
    file_path=[file_path for file_path in dir_path.iterdir() if file_path.is_file()]
    tasks=[asyncio.create_task(process_file(file_path)) for fille_path in file_path]
    await asyncio.gather(*tasks)

if __name__=='__main__':
    asyncio.run(main())