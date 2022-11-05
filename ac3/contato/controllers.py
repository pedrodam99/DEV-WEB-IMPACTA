from flask import render_template, request
from contato import contato_bp

@contato_bp.route('/form', methods=['GET'])
def form_get():
    print('Chamou o GET')
    return render_template('form.html')

@contato_bp.route('/form', methods=['POST'])
def form_post():
    dados = {
        'nome': request.form['nome'],
        'email': request.form['email'],
        'telefone': request.form['telefone'],
        'assunto': request.form['assunto'],
        'mensagem': request.form['mensagem'],
        'origem': request.form['origem']

    }

    print(dados)
    return render_template('contato.html', nome=dados['nome'])
