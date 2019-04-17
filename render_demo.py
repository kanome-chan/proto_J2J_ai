from flask import*

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def render_j2j():
    if request.method == "GET":
        return render_template("demo.html")
    elif request.method == "POST":
        words_dic = {"main":request.form["target_word"],"n1":"はたらく","n2":"仕事をする","n3":"労働","n4":"社畜","n5":"勉強","n6":"まなぶ"}
        return render_template("demo_2.html",words=words_dic)

if __name__ == "__main__":
    app.run(debug=True)
