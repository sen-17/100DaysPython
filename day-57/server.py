from flask import Flask, render_template
from datetime import datetime
import requests

app = Flask(__name__)
GENDER_URL = 'https://api.genderize.io'
AGE_URL = 'https://api.agify.io'
BLOG_URL = 'https://api.npoint.io/c790b4d5cab58020d391'

@app.route('/')
def home():
    now = datetime.now()
    current_year = now.year
    return render_template('index.html' , year = current_year)

@app.route('/guess/<name>')
def guess(name):
    params = {
        'name' : name
    }

    gender_response = requests.get(GENDER_URL, params)
    age_response = requests.get(AGE_URL, params)

    gender_data = gender_response.json()
    age_data = age_response.json()
    
    name_age = age_data['age']
    name_gender = gender_data['gender']

    return render_template('guess.html', gender = name_gender, age = name_age, name = name)

@app.route('/blog/<num>')
def blog(num):
    print(num)
    response = requests.get(BLOG_URL)
    data = response.json()
    return render_template('blog.html', post = data)

if __name__ == "__main__":
    app.run(debug=True)