from flask import Flask, jsonify, render_template, request, redirect, url_for

app = Flask(__name__)


# @app.route("/")
# def httpResponse():
#     return "<h1>this is flask first sssion</h1>"

@app.route("/json/")
def json():
    data = {
        "name" : "mahesh",
        "marks" : 30
    }

    return jsonify(data)



@app.route("/")
def index():
    customername = request.args.get("customername")
    data = {
        "name" : "mahesh",
        "marks" : 30
    }
    num = 40
    return render_template("index.html", userdata = data, val = num, customername = customername)

# {"userdata" : user}


@app.route("/main/", methods = ['POST', 'GET'])
def mainFun():
    if request.method == "POST":
        customername = request.form.get("customer")

        return redirect(url_for('index', customername = customername))
    

    return render_template("main.html")



if __name__ == "__main__" :
    app.run(debug=True, port=2000)

