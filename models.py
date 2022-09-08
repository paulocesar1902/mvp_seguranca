from base_template import db


class Emails(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name

