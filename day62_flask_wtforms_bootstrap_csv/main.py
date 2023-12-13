from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
bootstrap = Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe_name = StringField('Cafe Name', validators=[DataRequired()])
    location = URLField('Location', validators=[DataRequired()])
    open = StringField('Open', validators=[DataRequired()])
    close = StringField('Close', validators=[DataRequired()])
    coffee = StringField('Coffee', validators=[DataRequired()])
    wifi = StringField('Wifi', validators=[DataRequired()])
    power = StringField('Power', validators=[DataRequired()])
    submit = SubmitField('Add')


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.is_submitted():
        success_message = "Successfully added."
        new_cafe = [form.cafe_name.data, form.location.data, form.open.data, form.close.data, form.coffee.data,
                    form.wifi.data, form.power.data]
        new_cafe_record = '\n' + ','.join(new_cafe)
        print(new_cafe_record)
        with open('cafe-data.csv', 'a') as csv_file:
            csv_file.write(new_cafe_record)
        return render_template('added.html', form=form, message=success_message)

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
