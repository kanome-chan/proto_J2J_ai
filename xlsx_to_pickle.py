# In[]:
import openpyxl
book = openpyxl.load_workbook("data/D18-2018.7.24.xlsx")

# 今回は作業者Aのシートを使う
sheet = book["作業者A"]


# In[]:
dic = {}
for row in sheet.rows:
    dic[row[0].value] = tuple(row[2].value)
del dic["Word"]
# print(dic)

# In[]:
import pickle
with open("pickle/worker_a.pickle","wb") as f:
    pickle.dump(dic,f)
