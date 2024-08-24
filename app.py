from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# database connection and integration
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
db = SQLAlchemy(app)


class Student(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    student_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(100),nullable = False )
    contact = db.Column(db.Integer())


with app.app_context():
    db.create_all()


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


# crud application from here...

@app.route("/create-student/", methods = [ 'GET', 'POST' ])
def createStudent():
    if request.method == 'POST':
        student_name = request.form.get("student_name")
        email = request.form.get("email")
        contact = request.form.get("contact")

        student = Student(student_name = student_name, email = email, contact = contact)
        db.session.add(student)
        db.session.commit()


        return redirect(url_for("studentsData"))

    return render_template("crud/create-student.html")



@app.route("/students-data/")
def studentsData():
    students = Student.query.all()

    return render_template("crud/students-data.html", students = students)


# CreateStudent -- classname
# createStudent -- fun name


if __name__ == "__main__" :
    app.run(debug=True, port=2000)

