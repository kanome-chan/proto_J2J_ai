from flask import *
app = Flask(__name__)
import gensim

#読み込みにめっちゃ時間かかる
print("W2V読み込み中...")
model = gensim.models.KeyedVectors.load_word2vec_format("F:/vector/model.vec", binary=False)
print("W2V読み込み完了")


@app.route("/", methods=["GET", "POST"])
def odd_even():
    if request.method == "GET":
        return render_template("defult_form.html")
    else:
        try:
            word = request.form["word"]
            sim = model.most_similar(positive=[word])
            return render_template("return_form.html",word=request.form["word"],unnko=sim[0][0])
        except:
            return """
                    有効な入力ではありません！入力しなおしてください。
                    <form action="/" method="POST">
                    <input name="num"></input>
                    </form>"""


if __name__ == "__main__":
    app.run(debug=True)
