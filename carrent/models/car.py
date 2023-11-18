from carrent import db
from datetime import datetime

class Car(db.Model):
    id = db.Column(db.Integer ,primary_key=True)
    owner = db.Column(db.String(256), nullable=False)
    make = db.Column(db.String(128))
    model = db.Column(db.String(128))
    year = db.Column(db.Integer)
    description = db.Column(db.Text)
    daily_price = db.Column(db.Float)
    availability = db.Column(db.Boolean)
    date_posted = db.Column(db.Datetime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Car('{self.owner}', '{self.model}', '{self.date_posted}') "
