from flask import Flask, render_template, Request
from flask.globals import request
app = Flask(__name__)

@app.route('/')
def landing():
    return render_template('index.html')

@app.route('/sendemail', methods=['POST'])
def sendEmail():
    print(request.form['name'])
    return 'Email Sent!!! He will get back shortly'

if __name__ == 'main':
    app.run(debug=True)
