from flask import Flask, render_template, request
import requests
import smtplib

post_response = requests.get(f"https://api.npoint.io/1f1b63ab910f633adfc1").json()

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

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", bg_image='home-bg.jpg', all_posts=articles)


@app.route('/about')
def about():
    return render_template("about.html", bg_image='about-bg.jpg')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        confirm_msg = 'Successfylly sent your message'
        contact_message = (f"Message sent from Contact form:\n"
                           f"'{name}', \n"
                           f"email: '{email}',\n"
                           f"phone: {phone},\n"
                           f"message: {message}.</h1>")

        def send_email():
            my_email = "sergemoseratti@gmail.com"
            recipient_email = "moser@gmail.com"
            my_password = "ecre vjik cskb nswc"
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user=my_email, password=my_password)
                connection.sendmail(from_addr=my_email, to_addrs=recipient_email,
                                    msg=f"Subject: Message sent from Contact form.\n\n{contact_message}")

        send_email()
        return render_template("contact.html", bg_image='contact-bg.jpg', poster_msg=confirm_msg)
    elif request.method == 'GET':
        confirm_msg = 'Contact Me'
        return render_template("contact.html", bg_image='contact-bg.jpg', poster_msg=confirm_msg)


@app.route('/post/<int:post_id>')
def get_post(post_id):
    url_id = post_id
    post_obj = articles[post_id - 1]
    return render_template("post.html", bg_image='post-bg.jpg', post=post_obj, id=url_id)


if __name__ == "__main__":
    app.run(debug=True)
