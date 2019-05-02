from flask import*
import gensim
import pickle
import sys

app = Flask(__name__)
#読み込みにめっちゃ時間かかる
print("W2V読み込み中...")
try:
    model = gensim.models.KeyedVectors.load_word2vec_format("F:/vector/model.vec", binary=False)
except FileNotFoundError:
    print("SSDセットした？")
    sys.exit()
print("完了")


@app.route("/",methods=["GET","POST"])
def render_j2j():
    if request.method == "GET":
        return render_template("demo.html")
    elif request.method == "POST":
        try:
            target = request.form["target_word"]
            sim = model.most_similar(positive=[target],topn=100)
            sim2 = [_[0] for _ in sim] #単語のリスト
            word_list6 = sim2[:6]
            print(word_list6)
            n1,n2,n3,n4,n5,n6 = tuple(word_list6)
            words_dic = {"main":target,
                         "n1":n1,
                         "n2":n2,
                         "n3":n3,
                         "n4":n4,
                         "n5":n5,
                         "n6":n6,}
            return render_template("demo_2.html",words=words_dic)
        except:
            return render_template("demo_error.html")
    
if __name__ == "__main__":
    app.run()
