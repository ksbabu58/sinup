from flask import Flask, flash, redirect, render_template, request, session, abort
import os

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    return render_template('login.html')


@app.route('/login', methods=['POST','GET'])
def handle_form():
    if request.method == 'POST':
        username = request.form.get('uname')
        password = request.form.get('psw')
        return "login sucessful"
    else:
        return "Invalid request "

if __name__ == '__main__':
    app.run(debug=True)
    #, host='0.0.0.0', port=4000)
print(username)