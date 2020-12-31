from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('index.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

if __name__ == '__main__':
    app.run(debug=True)
