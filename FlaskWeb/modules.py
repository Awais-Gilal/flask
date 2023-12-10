from FlaskWeb import db

class Posts(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=120), unique=False, nullable=False)
    title = db.Column(db.String(length=999), unique=False, nullable=False)
    detail = db.Column(db.String(length=990), unique = False, nullable=False)
    date = db.Column(db.String(length=120), unique=False, nullable=False)


class Messages(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=120), unique = False, nullable=False)
    email = db.Column(db.String(length=120), unique=False, nullable=False)
    phone = db.Column(db.String(length=120), unique=False, nullable=False)
    message = db.Column(db.String(length=999), unique=False, nullable=False)
    date = db.Column(db.String(length=999), unique=False, nullable=False)