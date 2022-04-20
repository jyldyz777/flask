from flask import Flask, render_template
app = Flask(__name__)
@app.route('/say_hello')
def say_hello ():
    return '<h1>Hello,world!</h1>'

@app.route('/')
def index ():
    return render_template ('index.html')
