import requests
from bs4 import BeautifulSoup

PAGE_URL = "http://www.e-japanese.jp/?p=990"

html_doc = requests.get(PAGE_URL).text
soup = BeautifulSoup(html_doc,"html.parser")

with open("N4.txt","w",encoding="utf-8") as f:
    for link in soup.find_all("td")[::2]:
        f.write(link.get_text()+"\n")
