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

#2,4,5だけ
def make_text_from_html(word_difficulty,page_list):
    with open("text/"+word_difficulty+".txt","w",encoding="utf-8") as f:
        counter = 0
        for p in page_list:
            counter += 1
            PAGE_URL = "http://www.e-japanese.jp/?p={0}".format(p)
            html_doc = requests.get(PAGE_URL).text
            soup = BeautifulSoup(html_doc,"html.parser")
            for link in soup.find_all("td")[2::4]:
                txt = link.get_text()
                if only_japanese(txt.strip()):
                    f.write(txt+"\n")
            print(word_difficulty+" : {0}/{1}".format(counter,len(page_list)))
            time.sleep(1)
    print("="*10)

make_text_from_html("N5",[1005+i*3 for i in range(5)])
make_text_from_html("N4",[990+i*3 for i in range(5)])
N2list = [1028+i*3 for i in range(11)]
N2list.extend([1062,1065,1068])
make_text_from_html("N2",N2list)
