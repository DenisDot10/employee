from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.db'
    app.config['SECRET_KEY'] = '123'
    
    db.init_app(app)

    # Импортируем и регистрируем Blueprint
    from app.routes import main_bp
    app.register_blueprint(main_bp, url_prefix='/')
    
    return app