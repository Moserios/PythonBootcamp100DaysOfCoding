from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    post_response = requests.get(f"https://api.npoint.io/1f1b63ab910f633adfc1").json()
    return render_template("index.html", posts=post_response)


@app.route('/post/<post_id>')
def get_post(post_id):
    post_response = requests.get(f"https://api.npoint.io/1f1b63ab910f633adfc1").json()
    for post in post_response:
        if post['id'] == int(post_id):
            post_title = post['title']
            post_article = post['article']
            post_author = post['author']
            post_date = post['date']
    return render_template("post.html", title=post_title, article=post_article,
                           author=post_author, date=post_date)


if __name__ == "__main__":
    app.run(debug=True)
