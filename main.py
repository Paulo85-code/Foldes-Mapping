from flask import Flask
from routes import *
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///dados.db"
db = SQLAlchemy()
db.init_app(app)

class pastas_mapeamento(db.Model):
    __tablename__ = 'folderMapping'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40), nullable=False, unique=True)

if __name__ == "__main__":
    with app.app_context():
        user = pastas_mapeamento(nome='teste')
        db.session.add(user)
        db.session.commit()
        db.create_all()
    app.run(host='0.0.0.0', port=5000)