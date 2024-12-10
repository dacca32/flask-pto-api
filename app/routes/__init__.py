from flask import Blueprint

main = Blueprint('main', __name__)

from .auth import auth_bp
from .employee import employee_bp
from .pto import pto_bp

main.register_blueprint(auth_bp, url_prefix='/api/v1')
main.register_blueprint(employee_bp, url_prefix='/api/v1')
main.register_blueprint(pto_bp, url_prefix='/api/v1')

@main.route('/api/v1/test_route')
def your_function(): 
    return "Hello, World!"
