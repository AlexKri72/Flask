import  multiprocessing,time

def worker(num):
    print(f'Start process {num}')
    time.sleep(3)
    print(f'End process {num}')

if __name__ == '__main__':
    process=[]
    for i in range(5):
        p=multiprocessing.Process(target=worker,args=(i,))
        process.append(p)
        p.start()

    for p in process:
        p.join()

    print('All process ended')