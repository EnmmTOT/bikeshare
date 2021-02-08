from app import app
from flask import render_template


@app.route('/')
def re_error():
    user = {'username': 'grace'}
    return render_template('report_error.html', title='error', user=user)



