from flask import Flask, jsonify, render_template

app = Flask(__name__)


# @app.route("/")
# def httpResponse():
#     return "<h1>this is flask first sssion</h1>"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/json/")
def json():
    data = {
        "name" : "mahesh",
        "marks" : 30
    }

    return jsonify(data)




if __name__ == "__main__" :
    app.run(debug=True, port=2000)

