from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Dataset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(100))
    value = db.Column(db.Float)
