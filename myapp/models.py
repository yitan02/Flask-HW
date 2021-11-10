from myapp import db

class cities(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    city_name = db.Column(db.String(128), index = True)
    city_rank = db.Column(db.Integer, index = True)
    is_visited = db.Column(db.Boolean)

    def __repr__(self):
        return '<{self.city_name}>'