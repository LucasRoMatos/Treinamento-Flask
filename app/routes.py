from flask import render_template, flash, redirect, request
from app import app
from app.form import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user
from app.models import User
from flask_login import login_required
from werkzeug.urls import url_parse
from app import db


@app.route('/')
@login_required
def index():
    return render_template('index.html', home='Página Principal')
@app.route('/index')
@login_required
def off():
    return render_template('extends.html', home="Usuários off")

@app.route('/celular')
def cel():
    return render_template('celular.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/index')
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.nome.data).first()
        if user is None or not user.check_password(form.senha.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.lembredemim.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = 'index'
        return redirect(next_page)
    return render_template('formulario.html', home='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect('/index')


@app.route('/registrar', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect('index')
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect('login')
    return render_template('registrar.html', title='Register', form=form)

@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html', user=user, posts=posts)