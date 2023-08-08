import multiprocessing

counter = 0


def increment():
    global counter
    for _ in range(10_000):
        counter += 1
    print(f'�������� �������� : {counter:_}')


process = []
for i in range(5):
    p = multiprocessing.Process(target=increment)
    process.append(p)
    p.start()

for p in process:
    p.join()

print(f'�������� �������� � ������: {counter:_}')