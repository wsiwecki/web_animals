import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'wojsiwdb01.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'AnimalDB'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'animalTechUser'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or '@ns837c&shE3B'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'animalsstorage'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'LkBdLQ+z58p8RZpCDFgXHbMSS7VTuBUuhVyN4p536GgEs7+ZFy85kQf3BHoRI3YJzoXoaUzYOHLbNYakj0Jpmg=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'
