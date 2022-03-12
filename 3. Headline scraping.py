import bs4
import requests

url='https://en.wikipedia.org/wiki/Data_science'
data=requests.get(url)
soup=bs4.BeautifulSoup(data.text,'html.parser')

soup.select('.mw-headline')
for collection in soup.select('.mw-headline'):
    print(collection.text,end='\n')
