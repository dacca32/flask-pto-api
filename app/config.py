import os

class Config:
    JWT_SECRET_KEY = 'qwertyuioplkjhgfdsazxcvbnm'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///pto.db'
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_BLACKLIST_ENABLED = True
    FLASK_DEBUG = True
