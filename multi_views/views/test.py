from flask import render_template
from multi_views import app

@app.route('/test')
def test():
    return render_template('test.html')
