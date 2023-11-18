from carrent import db

class Location(db.Model):
    id = db.Column(db.Integer ,primary_key=True)
    name = db.Column(db.String(45))
    address = db.Column(db.Text)

    def __repr__(self):
        return f"Location('{self.name}', '{self.address}') "