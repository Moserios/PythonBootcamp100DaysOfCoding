from flask import Flask, render_template
from markupsafe import escape
import datetime
import requests

app = Flask(__name__)


@app.route("/")
def index():
    year = str(datetime.datetime.now()).split("-")[0]
    return render_template("index.html", current_year=year)


@app.route("/guess/<your_name>")
def guess_name(your_name):
    your_name = str(your_name).capitalize()
    age_response = requests.get(f"https://api.agify.io/?name={your_name}").json()
    extracted_age = age_response['age']
    gender_response = requests.get(f"https://api.genderize.io/?name={your_name}").json()
    extracted_gender = gender_response['gender']
    return render_template("name.html", name=your_name, gender=extracted_gender, age=extracted_age)


@app.route("/blog")
def blog():
    blog_response = requests.get(f"https://api.npoint.io/1f1b63ab910f633adfc1").json()
    return render_template("blog.html", blogs=blog_response)

if __name__ == "__main__":
    app.run(debug=True)
