# Создать программу, которая будет производить подсчет количества слов в каждом файле в указанной директории и выводить результаты в консоль.
# �спользуйте потоки.


import threading
from  pathlib import Path

def get_file_length(file_name):
    with open(file_name,'r',encoding='utf-8') as f:
        contens=f.read()
        print(f'{f.name} >>> {len(contens)} words')

if __name__=='__main__':
    threads=[]
    dir_path=Path('.')
    file=[file_path for file_path in dir_path.iterdir() if file_path.is_file()]

    for i in file:
        t = threading.Thread(target=get_file_length,args=(i,))
        threads.append(t)

    for i in  threads:
        i.start()

    for i in threads:
        i.join()

