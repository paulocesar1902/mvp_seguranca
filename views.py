import os
from flask import render_template, request, redirect, session, flash, url_for, send_from_directory
from base_template import app, db
from models import Emails
from helpers import FormularioEmail


@app.route('/')
def index():
    form = FormularioEmail()
    return render_template('index.html', titulo='index', form=form)


@app.route('/salvarEmail', methods=['POST',])
def salvarEmail():
    form = FormularioEmail(request.form)

    if not form.validate_on_submit():
        return redirect(url_for('index'))

    email = form.email.data

    novo_email = Emails(email=email)
    db.session.add(novo_email)
    db.session.commit()

    flash('Email cadastrado com sucesso!')

    return redirect(url_for('index'))