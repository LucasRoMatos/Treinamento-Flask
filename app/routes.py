from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {
        'username': 'Lucas',
        'idade': '18',
        'endereco': 'Mogi'
    }
    users = [
        {
        'username': 'Erika',
        'idade': '39',
        'endereco': 'Poa'
        },

        {
        'username': 'Rafael',
        'idade': '12',
        'endereco': 'Ferraz'
        }
    ]

    return render_template('index.html', user=user, home='Página Principal', users=users)