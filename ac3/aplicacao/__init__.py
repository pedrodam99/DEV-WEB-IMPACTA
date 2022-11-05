from flask import Flask

from contato import contato_bp
from cursos import cursos_bp

app = Flask('aplicacao')
app.config.from_object('aplicacao.config.Configuracao')

app.register_blueprint(contato_bp)
app.register_blueprint(cursos_bp)