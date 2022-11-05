from app import app
from flask import render_template, request

@app.route('/ola')
@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/form', methods=['GET'])
def form_get():
    print('Chamou o GET')
    return render_template('form.html')

@app.route('/form', methods=['POST'])
def form_post():
    print('Isso é um POST feito por', request.form['nome'])
    return render_template('form.html')