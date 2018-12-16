from datetime import datetime

from brood_backend.database import db


class Peck(db.Model):

    uuid = db.Column(db.String(length=36), primary_key=True)
    created = db.Column(
        db.DateTime, unique=False, nullable=False, default=datetime.utcnow
    )
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(length=1), nullable=False)
    # chicken_uuid = db.Column(db.String, db.ForeignKey("chicken.uuid"))
    # chicken = db.relationship("Chicken", backref="peck")

    def to_dict(self) -> dict:
        return {
            "uuid": self.uuid,
            "created": self.created,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "chicken": "TODO",
        }
