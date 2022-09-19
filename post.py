import requests
import json
import base64


#Staks edition -------------------
import csv
import sys

import requests


def get_post_my_tips(link):
    with open('url_image.csv', 'r', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            url_image_moment = ', '.join(row)
            print(url_image_moment)

            data = {
                'title': 'like',
                'content': 'something2',
            }
            try:
                response = requests.post(link, json=data, files={'image': url_image_moment})

                print(response, str(response.json()))

            except:
                print(sys.exc_info())


if __name__ == "__main__":
    link = 'https://my-tips.ru/test'
    get_post_my_tips(link=link)
#Staks edition -----------------------------------------------








link = 'http://127.0.0.1:8000/test'
image = open('images/randompic.jpg','rb')

data = {
	'title' : 'like',
	'content' : 'something2',
}

response = requests.post(link, json=data, files={'image': image, },)

print(response, response.json())


# link = 'http://127.0.0.1:8000/test'


# data = {
# 	'title' : 'like',
# 	'content' : 'something2',
# }


# image_file = 'images/randompic.jpg'

# with open(image_file, "rb") as f:
# 	im_bytes = f.read()
# im_b64 = base64.b64encode(im_bytes).decode("utf8")

# headers = {'Content-type': 'application/json',}
  
# payload = json.dumps({"image": im_b64,'title' : 'like',
# 	'content' : 'something2',})

# response = requests.post(link, data=payload, headers=headers)


# # response = requests.post(link, json=data, files={'image': image},  )

# print(response,)
