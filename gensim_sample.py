import gensim
model = gensim.models.KeyedVectors.load_word2vec_format("F:/vector/model.vec",binary=False)
sim = model.most_similar(positive=["高専"])
print(sim)
for _ in sim:
    print(_[0])
