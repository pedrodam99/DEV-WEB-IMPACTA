from flask import render_template

from admin import admin_bp

@admin_bp.route('/')
def admin():
    return render_template('admin.html')