from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result",  methods=['POST'])
def page():
    print("info")
    print(request.form)
    Your_Name_from_form = request.form['Your_Name']
    Dojo_location_from_form = request.form['Dojo_location']
    Favorite_language_from_form = request.form['Favorite_language']
    return render_template("survey.html", Your_Name_on_template=Your_Name_from_form, Dojo_location_on_template=Dojo_location_from_form, Favorite_language_on_template=Favorite_language_from_form)


if __name__ == "__main__":
    app.run(debug=True)