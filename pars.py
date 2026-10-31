import requests
from bs4 import BeautifulSoup
url="http://192.168.0.105:5000/autorisation"
r = requests.get(url)
soup=BeautifulSoup(r.text,"html.parser")
print(soup.find("h1"))