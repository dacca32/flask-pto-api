import os

class Config:
    JWT_SECRET_KEY = 'qwertyuioplkjhgfdsazxcvbnm'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://scot:password123!@localhost:5432/pto_db'
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_BLACKLIST_ENABLED = True
    FLASK_DEBUG = True
