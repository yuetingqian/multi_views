from flask import render_template
from multi_views import app

@app.route('/')
def index():
    return render_template('login.html')
