from carrent import db

class Reservation(db.Model):
    id = db.Column(db.Integer ,primary_key=True)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    car_id = db.Column(db.Integer, db.ForeignKey('car.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'), nullable=False)

    def __repr__(self):
        return f"Reservation('{self.start_date}', '{self.end_date}') "
