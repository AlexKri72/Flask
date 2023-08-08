import random,time

def long_running_task():
    for i in range(5):
        print(f'working task {i}')
        time.sleep(random.randint(1,3))

def main():
    print('Start program')
    long_running_task()
    print('End program')

main()