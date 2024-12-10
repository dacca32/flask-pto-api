from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager, jwt_required,create_access_token, get_jwt_identity, get_jwt

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
