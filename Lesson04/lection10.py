import asyncio

async  def count():
    print('Start')
    await asyncio.sleep(1)
    print('go 1 sec')
    await asyncio.sleep(2)
    print('go next 2 sec')
    return 'Ready'

async  def main():
    result= await asyncio.gather(count(),count(),count())
    print(result)

asyncio.run(main())