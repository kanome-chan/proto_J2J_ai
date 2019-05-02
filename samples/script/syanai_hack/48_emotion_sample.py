from flask import Flask,render_template,redirect,request
import pickle

app = Flask(__name__)

with open("pickle/作業者A.pickle","rb") as f:
    emotion_dic = pickle.load(f)

@app.route("/",methods=["GET","POST"])
def default():
    if request.method == "GET":
        return render_template("48e_default.html")
    else:
        word = request.form["target_word"]
        try:
            emotion = emotion_dic[word]
            return render_template("48e_answer.html",emotion=emotion[0])
        except KeyError:
            return render_template("48e_error.html",word=word)

if __name__ == "__main__":
    app.run(debug=True)