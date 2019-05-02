import gensim

#読み込みにめっちゃ時間かかる
model = gensim.models.KeyedVectors.load_word2vec_format("F:/vector/model.vec", binary=False)

word = "高専"
sim = model.most_similar(positive=[word])
for _ in sim:
    print(_[0])
