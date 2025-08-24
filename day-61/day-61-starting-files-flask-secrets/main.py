from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(allow_empty_local=True)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField("Log In", validators=[DataRequired()] )

app = Flask(__name__)
app.secret_key = "123456"

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@email.com":
            if form.password.data == "12345678":
                return render_template('success.html')
        else:
            return render_template('denied.html')

    return render_template('login.html', form=form)    

if __name__ == '__main__':
    app.run(debug=True)
