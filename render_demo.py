from flask import*
import gensim
import pickle

app = Flask(__name__)
#読み込みにめっちゃ時間かかる
print("W2V読み込み中...")
try:
    model = gensim.models.KeyedVectors.load_word2vec_format("F:/vector/model.vec", binary=False)
except FileNotFoundError:
    print("SSDセットした？")
print("完了")


print("難易度読み込み中...")
with open("pickle/N5.pickle","br") as f:
    N5_list = pickle.load(f)
with open("pickle/N4.pickle","br") as f:
    N4_list = pickle.load(f)
with open("pickle/N2.pickle","br") as f:
    N2_list = pickle.load(f)
difficulty_list = [N5_list,N4_list,N2_list]
print("完了")


@app.route("/",methods=["GET","POST"])
def render_j2j():
    if request.method == "GET":
        return render_template("demo.html")
    elif request.method == "POST":
        target = request.form["target_word"]
        sim = model.most_similar(positive=[target],topn=300)
        sim2 = [_[0] for _ in sim] #単語のリスト
        word_list6 = []
        for n_list in difficulty_list:
            for word in sim2:
                if word in n_list:
                    word_list6.append(word)
                    if len(word_list6)>=6:
                        break
        n1,n2,n3,n4,n5,n6 = tuple(word_list6)
        words_dic = {"main":target,
                     "n1":n1,
                     "n2":n2,
                     "n3":n3,
                     "n4":n4,
                     "n5":n5,
                     "n6":n6,}
        return render_template("demo_2.html",words=words_dic)

if __name__ == "__main__":
    app.run()
