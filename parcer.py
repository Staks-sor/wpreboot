from bs4 import BeautifulSoup
import requests
import os 
import random
import csv
import shutil



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

# Получаем адрес страницы
page = requests.get(f'https://the-moment.ru/sitemap.html')
soup = BeautifulSoup(page.text, 'lxml')

print("Получаем ссылки")


#заходим в каждый "отдел" где посты рассортированы по месяцам
for posts_in_month in soup.select('td > a')[1::]:
    response = requests.get(posts_in_month['href'])
    soup = BeautifulSoup(response.text, 'lxml')

    #вытаскиваем пост из каждого месяца
    for post in soup.select('td > a'):
        post_page = requests.get(post['href'])
        post_soup = BeautifulSoup(post_page.text, 'lxml')
        print(f"{post['href']}\n\n")


        for elem in (post_soup.select(".site-content > .site-content-inner > .content-area > .site-main > article")):
            print('Получаем заголовок статьи')
            title = elem.select(".entry-header > h1")
            # print(f'{title[0].text}\n\n')

            # print('Получаем текст статьи')
            text = elem.select(".entry-content")
            # print(f"{text[0].text}\n\n")

            print("Получаем картинки статьи")   

            imagelinks = []
            for img in elem.find_all('img', src=True, ):
                print(f"{img['src']}\n\n")
                download_images(img['src'])

        print(f"все данные взяты с данной страниы {post['href']}\n\n")
