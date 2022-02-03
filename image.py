from bs4 import BeautifulSoup
import requests as rq 
import os

r2 = rq.get('https://www.carlogos.org/start-with-a',headers={"User-Agent": "XY"})
soup2 = BeautifulSoup(r2.text, 'html.parser')

links = []
link = [1,2,3]

x = soup2.select('img[src^="/car-logos"]')

for img in x:
    links.append('https://www.carlogos.org' + img['src'])

# for l in links:
#     print(l)
img_test = []
os.makedirs('car-logo-a')
for index, img_link in enumerate(links):
    img_data = rq.get(img_link,headers={"User-Agent": "XY"}).content
    img_test = img_link.split("/")
    with open("car-logo-a\\"+ str(img_test[4]), 'wb+') as f:
        f.write(img_data) 


