import openpyxl
import pickle

def xlsx_to_pickle(worker_name):
    book = openpyxl.load_workbook("data/D18-2018.7.24.xlsx")
    sheet = book[worker_name]
    word_dic = {}
    for row in sheet.rows:
        word_dic[row[0].value] = tuple(row[2].value)
    del word_dic["Word"]
    with open("pickle/{0}.pickle".format(worker_name),"wb") as f:
        pickle.dump(word_dic,f)

xlsx_to_pickle("作業者A")
xlsx_to_pickle("作業者B")
xlsx_to_pickle("作業者C")
