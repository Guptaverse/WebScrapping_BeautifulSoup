# from bs4 import BeautifulSoup
# import requests


# website = "https://subslikescript.com/movie/Titanic-120338"

# res = requests.get(website)
# content = res.text
# soup = BeautifulSoup(content,'lxml')

# print(soup.prettify())

# box = soup.find('article',class_ = 'main-article')

# title = box.find('h1').get_text()

# transcript = box.find('div',class_ = 'full-script').get_text(strip = True,separator=' ')

# with open(f'{title}.txt','w',encoding='utf-8') as file:
#     file.write(transcript)    

#for multiple pages


from bs4 import BeautifulSoup
import requests

root = "https://subslikescript.com"
website = f"{root}/movies"

res = requests.get(website)
content = res.text
soup = BeautifulSoup(content,'lxml')

# print(soup.prettify())

box = soup.find('article',class_ = 'main-article')



links = []

for link in box.find_all('a',href=True):
    links.append(f"{root}/{link['href']}")

print(len(links))

for link in links:
    website = link
    res = requests.get(website)
    content = res.text
    soup = BeautifulSoup(content,'lxml')
    box = soup.find('article',class_= 'main-article')

    title = box.find('h1').get_text()
    transcript = box.find('div',class_ = 'full-script').get_text(strip = True,separator=' ')
    with open(f'{title}.txt','w',encoding='utf-8') as file:
        file.write(transcript)
