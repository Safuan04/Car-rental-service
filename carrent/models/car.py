from carrent import db
from datetime import datetime

class Car(db.Model):
    id = db.Column(db.Integer ,primary_key=True)
    make = db.Column(db.String(128))
    model = db.Column(db.String(128))
    year = db.Column(db.Integer)
    description = db.Column(db.Text)
    daily_price = db.Column(db.Float)
    availability = db.Column(db.Boolean)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    img_file = db.Column(db.String(256), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('owner.id'), nullable=False)

    def __repr__(self):
        return f"Car('{self.make}', '{self.model}', '{self.date_posted}')"
