import requests
from bs4 import BeautifulSoup
import time

#アルファベットのリスト
alphabet_list = list("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM") 

def only_japanese(doc):
    if doc == "":
        return False
    for char in list(doc):
        if char in alphabet_list:
            return False
    return True

#アルファベット抜きの単語帳
def make_text_from_html(word_difficulty,number_of_pages,first_page_query):
    with open(word_difficulty+".txt","w",encoding="utf-8") as f:
        for i in range(number_of_pages):
            PAGE_URL = "http://www.e-japanese.jp/?p={0}".format(first_page_query+i*3)
            html_doc = requests.get(PAGE_URL).text
            soup = BeautifulSoup(html_doc,"html.parser")
            for link in soup.find_all("td")[2::4]:
                txt = link.get_text()
                if only_japanese(txt.strip()):
                    f.write(txt+"\n")
            print(word_difficulty+" : {0}/{1}".format(i+1,number_of_pages))
            time.sleep(0.5)
    print("="*10)

make_text_from_html("N5",5,1005)
make_text_from_html("N4",5,990)
