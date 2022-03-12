import bs4
import requests

url='https://en.wikipedia.org/wiki/Data_science'
data=requests.get(url)
soup=bs4.BeautifulSoup(data.text,'html.parser')

for items in soup.find_all('p'):
    print(items.text)
