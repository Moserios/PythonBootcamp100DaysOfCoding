from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap5


class LoginForm(FlaskForm):
    username = EmailField(label='Email', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label="Log in")


app = Flask(__name__)
app.secret_key = "my-secret-key-string"
bootstrap = Bootstrap5(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    my_form = LoginForm()
    # print("initiated")
    if my_form.is_submitted() is True:
        if my_form.username.data == "admin@admin.com" and my_form.password.data == "1234567890":
            # print("success")
            return render_template('success.html')
        else:
            # print("denied")
            return render_template('denied.html')
    # else:
    return render_template('login.html', form=my_form)


if __name__ == '__main__':
    app.run(debug=True)
