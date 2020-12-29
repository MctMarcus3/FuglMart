from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/local')
def home():
    return "<h1>Local File</>"

if __name__ == '__main__':
    app.run(debug=True)
