from app import db


class Bike(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    Location = db.Column(db.String(64), index=True, unique=True)
    Street = db.Column(db.String(64), index=True, unique=True)
    Distance = db.Column(db.Integer, index=True, unique=True)
    Area = db.Column(db.String(64), index=True, unique=True)
    Status = db.Column(db.String(64), index=True, unique=True)

    def __repr__(self):
        return '<Bike {}>'.format(self.ID)
