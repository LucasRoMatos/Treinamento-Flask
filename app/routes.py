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

    prefere = [
        {
        'esporte':'futebol',
        'musica': 'rap',
        'cor':'preto',
        'passeio':'sítio'
        },

        {
        'esporte':'futebol',
        'musica': 'rap',
        'cor':'preto',
        'passeio':'sítio'
        }
    ]
    return render_template('index.html', user=user, home='Página Principal', prefere=prefere)