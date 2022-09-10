import requests
import json
import base64


link = 'http://127.0.0.1:8000/test'
image = open('images/randompic.jpg','rb')

data = {
	'title' : 'like',
	'content' : 'something2',
}

response = requests.post(link, json=data, files={'image': image},)

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