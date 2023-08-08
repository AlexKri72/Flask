# Написать программу, которая скачивает изображения с заданных URL-адресов и сохраняет их на диск.
# Каждое изображение должно сохраняться в отдельном файле, название которого соответствует названию изображения в URL-адресе.
# Например URL-адрес: https://example/images/image1.jpg -> файл на диске: image1.jpg
# Программа должна использовать многопоточный, многопроцессорный и асинхронный подходы.
# Программа должна иметь возможность задавать список URL-адресов через аргументы командной строки.
# Программа должна выводить в консоль информацию о времени скачивания каждого изображения и общем времени выполнения программы.
import  requests,time,asyncio

urls=['https://i.pinimg.com/originals/37/12/c2/3712c24f3c989ea7374e843f4d3deabd.jpg',
      'https://i.artfile.ru/3872x2581_721133_[www.ArtFile.ru].jpg',
      'https://w.forfun.com/fetch/9d/9d960b0aead8ec236c3029fb7985dba3.jpeg',
      'https://w-dog.ru/wallpapers/1/11/508407145702532/bugatti-veyron-sportivnyj-avtomobil-avto-doroga-pustynya-pesok-skorost.jpg',
      'https://w.forfun.com/fetch/17/178ab665d14f6c46c08150a6ee9b22c1.jpeg'
]

async def get_img(url):
    img_start_time=time.time()
    responce = requests.get(url)
    filename = 'async_' + url.split('/')[-1]
    with open(filename, 'wb') as f:
        f.write(responce.content)
    print(f'downloaded {url} >>> {time.time() - img_start_time:.2f} second')

if __name__=='__main__':
    start_time = time.time()

    tasks=[]
    for url in urls:
        task=asyncio.ensure_future(get_img(url))
        tasks.append(task)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))

    print(f'downloaded all imges in threading >>> {time.time() - start_time:.2f} second')
