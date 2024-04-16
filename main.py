import requests
from bs4 import BeautifulSoup

url = "https://www.wildberries.ru/catalog/0/search.aspx?search=msi"

headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}
req = requests.get(url, headers=headers)
src = req.text
print(src)