import openpyxl
import pickle

def xls_to_pickle():
    book = openpyxl.load_workbook("data/D2-2014.8.12.xlsx")
    sheet = book.active
    word_dic = {}
    for row in sheet.rows:
        word_dic[row[0].value] = row[2].value
    with open("pickle/{0}.pickle".format("change_other_word"),"wb") as f:
        pickle.dump(word_dic,f)

xls_to_pickle()