import os
import pickle

def saiki_load(file_path):
    try:
        with open(file_path,"rb") as f:
            print(pickle.load(f))
    except:
        os.chdir("../")
        saiki_load(file_path=file_path)
    finally:
        print(os.getcwd())

saiki_load("pickle/N4.pickle")