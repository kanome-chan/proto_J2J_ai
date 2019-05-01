import gensim
import pickle

#読み込みにめっちゃ時間かかる
model = gensim.models.KeyedVectors.load_word2vec_format("F:/vector/model.vec", binary=False)

with open("pickle/N5.pickle","br") as f:
    N5_list = pickle.load(f)
with open("pickle/N4.pickle","br") as f:
    N4_list = pickle.load(f)
with open("pickle/N2.pickle","br") as f:
    N2_list = pickle.load(f)

word = "仕事"
sim = model.most_similar(positive=[word],topn=300)
sim2 = [_[0] for _ in sim]

difficulty_list = [N5_list,N4_list,N2_list]

counter = 0
for n_list in difficulty_list:
    counter += 1
    for word in sim2:
        if word in n_list:
            print(counter,word)
    print("="*10)
