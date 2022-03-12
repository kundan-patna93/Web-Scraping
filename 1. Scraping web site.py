import bs4
import requests

url="https://mail.google.com/mail/u/0/#inbox"
data=requests.get(url)
soup=bs4.BeautifulSoup(data.text,'html.parser')
print(soup.prettify())
