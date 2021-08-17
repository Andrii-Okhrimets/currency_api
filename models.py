from app import db


class Current(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    currency = db.Column(db.String(10))
    price = db.Column(db.String(20))
    date = db.Column(db.DateTime, default=datetime.now().date())

    def __repr__(self):
        return f'<current {self.id}>'
