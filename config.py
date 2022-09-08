import os

SECRET_KEY = 'projeto'

SQLALCHEMY_DATABASE_URI = \
    '{SGDB}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGDB = 'mysql+mysqlconnector',
        usuario = 'teste',
        senha = '1234',
        servidor = 'localhost',
        database = 'base_template'
    )
