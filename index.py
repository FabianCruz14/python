# first, we import a framework flask with a next steps

from flask import Flask

# app is a init name to a main file
app = Flask(__name__)

# create a route
@app.route('/')
def index():
    return 'Hello World'

@app.route('/aboutme')
def aboutMe():
    return 'About me'

if __name__== '__main__':
    app.run()