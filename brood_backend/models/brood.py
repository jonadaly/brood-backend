from datetime import datetime

from brood_backend.database import db


class Brood(db.Model):

    uuid = db.Column(db.String(length=36), primary_key=True)
    created = db.Column(
        db.DateTime, unique=False, nullable=False, default=datetime.utcnow
    )
    name = db.Column(db.String(), unique=False, nullable=False)
    hashed_password = db.Column(db.String(), unique=False, nullable=False)
    chickens = db.relationship("Chicken", back_populates="brood")

    def to_dict(self) -> dict:
        return {
            "uuid": self.uuid,
            "created": self.created,
            "name": self.name,
            "chickens": sorted([c.to_dict() for c in self.chickens], key=lambda x: x["created"]),
        }
