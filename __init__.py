from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/local')
def home():
    return "<h1>Local File</>"

@app.route('/Test')
def home():
    return "<h1>Local File</>"

@app.route('/login')
def login():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
