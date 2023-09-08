from flask import Flask , render_template , request , flash

app = Flask(__name__)

app.secret_key = "mashdali123"
@app.route('/profesearch')
def index():
    flash("hi")
    return render_template("index.html")

@app.route("/profesearch",methods=["POST" , "GET"])
def answer():
    flash("this is the query:" + str(request.form["search"]))
    return render_template("index.html")
# def home():
#     return "Flask heroku app"


# if __name__ == '__main__':
#     app.run()