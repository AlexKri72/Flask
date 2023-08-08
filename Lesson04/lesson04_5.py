# Создать программу, которая будет производить подсчет количества слов в каждом файле в указанной директории и выводить результаты в консоль.
# используйте процессы.


import multiprocessing
from  pathlib import Path

def get_file_length(file_name):
    with open(file_name,'r',encoding='utf-8') as f:
        contens=f.read()
        print(f'{f.name} >>> {len(contens)} words')

if __name__=='__main__':
    processes=[]
    dir_path=Path('.')
    file=[file_path for file_path in dir_path.iterdir() if file_path.is_file()]

    for i in file:
        p = multiprocessing.Process(target=get_file_length,args=(i,))
        processes.append(p)

    for i in  processes:
        i.start()

    for i in processes:
        i.join()

