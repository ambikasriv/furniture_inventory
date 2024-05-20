from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import routes
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///furniture.db'
    app.config['SECRET_KEY'] = 'srivastava'
    db.init_app(app)
    
    with app.app_context():
        from .routes import main
        app.register_blueprint(main)
        db.create_all()
    
    return app




app = create_app()

if __name__ == "__main__":
    app.run(debug=True)

