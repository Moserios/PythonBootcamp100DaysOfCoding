from flask import Flask, render_template
import requests


post_response = requests.get(f"https://api.npoint.io/1f1b63ab910f633adfc1").json()
# print(post_response)
articles = []
for post in post_response:
    new_article = []
    new_article.append(post['id'])
    new_article.append(post['title'])
    new_article.append(post['subtitle'])
    new_article.append(post['article'])
    new_article.append(post['author'])
    new_article.append(post['date'])
    articles.append(new_article)
# print(articles)

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", bg_image='home-bg.jpg', all_posts=articles)

@app.route('/about')
def about():
    return render_template("about.html", bg_image='about-bg.jpg')

@app.route('/contact')
def contact():
    return render_template("contact.html", bg_image='contact-bg.jpg')

@app.route('/post/<int:post_id>')
def get_post(post_id):
    url_id = post_id
    post_obj = articles[post_id-1]
    return render_template("post.html", bg_image='post-bg.jpg', post=post_obj, id=url_id)


if __name__ == "__main__":
    app.run(debug=True)
