import pickle
def text_to_pickle(file_name):
    with open(file_name,"r",encoding="utf-8") as f:
        word_list = [line.strip() for line in f.readlines()]
        print(word_list)

    pickle_file = "pickle/"+file_name[5:-3]+"pickle"
    with open(pickle_file,"wb") as f:
        pickle.dump(word_list,f)
text_to_pickle("text/N5.txt")
text_to_pickle("text/N4.txt")
text_to_pickle("text/N2.txt")

"""
with open("N5.pickle","rb") as f:
    a = pickle.load(f)
    print(a)
"""
