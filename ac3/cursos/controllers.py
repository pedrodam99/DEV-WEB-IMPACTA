from flask import render_template
from cursos import cursos_bp

@cursos_bp.route('/')
def index():
    return render_template('home.html')