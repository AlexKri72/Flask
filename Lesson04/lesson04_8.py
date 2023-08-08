# Напишите программу на Python, которая будет находить сумму элементов массива из 1000000 целых чисел.
# пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# массив должен быть заполнен случайными целыми числами от 1 до 100.
# при решении задачи нужно использовать многопоточность, многопроцессорность и асинхронность.
# в каждом решении нужно вывести время выполнения вычислений.

import asyncio,time,random

massive=[random.randint(1, 101) for _ in range(1000000)]
sum=0
async def summa(arr):
    global sum
    for i in arr:
        sum+=i


if __name__=='__main__':

    start_time=time.time()
    tasks=[]
    for i in range(10):
        start_index=i*100000
        end_index=start_index+100000
        task =asyncio.ensure_future(summa(massive[start_index:end_index]))
        tasks.append(task)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    print(f'async >>> {sum} time>>> {time.time()-start_time}')
