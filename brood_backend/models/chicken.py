from datetime import datetime

from brood_backend.database import db


class Chicken(db.Model):

    uuid = db.Column(db.String(length=36), primary_key=True)
    created = db.Column(
        db.DateTime, unique=False, nullable=False, default=datetime.utcnow
    )
    name = db.Column(db.String(), unique=False, nullable=False)
    pecks = db.relationship("Peck", back_populates="chicken")
    brood_uuid = db.Column(db.String, db.ForeignKey("brood.uuid"), nullable=False)
    brood = db.relationship("Brood", back_populates="chickens")

    def to_dict(self) -> dict:
        return {"uuid": self.uuid, "created": self.created, "name": self.name}
