from carrent import db

class Reservation(db.Model):
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)

    def __repr__(self):
        return f"Reservation('{self.start_date}', '{self.end_date}') "
