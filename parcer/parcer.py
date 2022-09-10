import datetime
from bs4 import BeautifulSoup
import requests
import os
import random
import csv
import shutil
import traceback
import base64
import json

FILE_CSV_NAME = "in.csv"
DIR = 'images'


def download_images(imagelink):

    if not os.path.exists("images"):
        os.mkdir("images")

    try:
        response = requests.get(imagelink)
    except OSError:
        path = r"random_img"
        filename = random.choice([
            x for x in os.listdir(path)
            if os.path.isfile(os.path.join(path, x))
        ])
        shutil.copy(f"random_img/{filename}", f"images/{filename}")
    else:
        imagename = f'images/{imagelink.split("/")[-1]}'
        with open(imagename, 'wb') as file:
            file.write(response.content)

def post_data(title, content,image):
    link = 'http://127.0.0.1:8000/test'


    data = {
        'title' : f'{title}',
        'content' : f'{content}',
    }

    im_b64 = []
    for i in image:
        image_file = f'images/randompic.jpg'
        
        with open(image_file, "rb") as f:
            im_bytes = f.read()
        im_b64.append(base64.b64encode(im_bytes).decode("utf8"))

    headers = {'Content-type': 'application/json',}
    
    payload = json.dumps({"image": im_b64,'title' : f'{title}',
        'content' : f'{content}',})

    response = requests.post(link, data=payload, headers=headers)
    
    return requests.post(link, data=payload, headers=headers)


with open(FILE_CSV_NAME, mode='r', encoding='utf-8') as r_file:
    # Создаем объект reader, указываем символ-разделитель ","
    file_reader = csv.reader(r_file, delimiter=";", quotechar='|')
    for row in file_reader:
        url = row[0]
        print(row[0])

        # Получаем адрес страницы
        page = requests.get(f'{(str(url))}')
        soup = BeautifulSoup(page.text, 'lxml')
        # print(soup)

        print("Получаем ссылки")

        try:
            for elem in (soup.select(".site-content > .site-content-inner > .content-area > .site-main > article")):
                print('Получаем заголовок статьи')
                title = elem.select(".entry-header > h1")
                print(f'{title[0].text}\n\n')

                # print('Получаем текст статьи')
                text = elem.select(".entry-content")
                print(f"{text[0].text}\n\n")

                print("Получаем картинки статьи")

                imagelinks = []
                for img in elem.find_all('img', src=True, ):
                    print(f"{img['src']}\n\n")
                    imagelinks.append(img['src'])
                    download_images(imagelinks)
                    # download_images(img['src'])
                post_data(title[0].text, text[0].text, imagelinks)

            # print(f"все данные взяты с данной страниы {post['href']}\n\n")
        except Exception as e:
            print(traceback.format_exc())
            with open('log.txt', mode='a', encoding='utf-8') as w_file:
                file_writer = csv.writer(w_file, delimiter=";", lineterminator="\r")
                file_writer.writerow([f"{traceback.format_exc()}\n", f'date: {datetime.datetime.now}\n\n'])