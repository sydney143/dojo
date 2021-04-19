from flask import Flask, render_template, request, redirect,flash
from mysqlconnection import connectToMySQL
app = Flask(__name__)
app.secret_key = "keep it secret"

@app.route("/")
def index():
    mysql = connectToMySQL ('survey')
    survey = mysql.query_db('SELECT * FROM dojo_survey;')
    print(survey)
    return render_template("index.html", all_survey=survey)


@app.route("/result",  methods=['POST'])
def page():
    is_valid = True		# assume True
    if len(request.form['name']) < 1:
    	is_valid = False
    	flash ("Please enter full name")
    if len(request.form['location']) < 1:
    	is_valid = False
    	flash ("Please enter location")
    if len(request.form['language']) < 2:
    	is_valid = False
    	flash ("Please enter favorite language")
    
    if is_valid:

        query = "INSERT  INTO survey ( name, location, language, created_at, updated_at) VALUES (%(name)s, %(location)s, %(language)s, NOW(), NOW();)"
        data = {
            'name': request.form['name'],
            'location': request.form['location'],
            'language': request.form['language']
        }
        db= connectToMySQL('survey')
        db.query_db(query,data)
        return render_template("survey.html")

    return redirect('/')

    


if __name__ == "__main__":
    app.run(debug=True)