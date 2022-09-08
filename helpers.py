import os
from base_template import app
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, validators


class FormularioEmail(FlaskForm):
    email = StringField('Email', [validators.data_required(), validators.Length(min=1, max=50)])
    salvar = SubmitField('Enviar')