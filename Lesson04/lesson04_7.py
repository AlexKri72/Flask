# Напишите программу на Python, которая будет находить сумму элементов массива из 1000000 целых чисел.
# пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...] массив должен быть заполнен случайными целыми числами от 1 до 100.
# при решении задачи нужно использовать многопоточность, многопроцессорность и асинхронность.
# в каждом решении нужно вывести время выполнения вычислений.

import threading,multiprocessing,asyncio,time,random

massive=[random.randint(1, 101) for _ in range(1000000)]
sum=0
def summa(arr):
    global sum
    for i in arr:
        sum+=i


if __name__=='__main__':

    start_time=time.time()
    threadings=[]
    for i in range(10):
        start_index=i*100000
        end_index=start_index+100000
        thread =threading.Thread(target=summa,args=(massive[start_index:end_index],))
        threadings.append(thread)
        thread.start()

    for i in threadings:
        i.join()
    print(f'thread >>> {sum} time>>> {time.time()-start_time}')

    start_time=time.time()
    processes=[]
    for i in range(10):
        start_index=i*100000
        end_index=start_index+100000
        p =multiprocessing.Process(target=summa,args=(massive[start_index:end_index],))
        processes.append(p)

    for i in  processes:
        i.start()

    for i in processes:
        i.join()
    print(f'processes >>> {sum} time>>> {time.time()-start_time}')