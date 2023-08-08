import threading,time

def worker(num):
    print(f'Start stream {num}')
    time.sleep(3)
    print(f'End stream {num}')

threads=[]
for i in range(5):
    t= threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print('All streams ended')