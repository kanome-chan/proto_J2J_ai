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


@app.route("/", methods=["GET", "POST"])
def odd_even():
    if request.method == "GET":
        return render_template("defult_form.html")
    elif request.method == "POST":
        try:
            target = request.form["input_word"]
            print(target)
            sim = model.most_similar(positive=[target],topn=1000)
            sim2 = [_[0] for _ in sim]
            for n_list in difficulty_list:
                for near_word in sim2:
                    if near_word in n_list:
                        return render_template("return_form.html",word=target,unnko=near_word)
        except:
            return render_template("defult_form.html")
if __name__ == "__main__":
    app.run()
