"""Added chicken and brood tables

Revision ID: 8b2df516c612
Revises: c3c492ce2dc4
Create Date: 2018-12-16 22:03:51.571162

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "8b2df516c612"
down_revision = "c3c492ce2dc4"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "brood",
        sa.Column("uuid", sa.String(length=36), nullable=False),
        sa.Column("created", sa.DateTime(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("hashed_password", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("uuid"),
    )
    op.create_table(
        "chicken",
        sa.Column("uuid", sa.String(length=36), nullable=False),
        sa.Column("created", sa.DateTime(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("brood_uuid", sa.String(), nullable=True),
        sa.ForeignKeyConstraint(["brood_uuid"], ["brood.uuid"]),
        sa.PrimaryKeyConstraint("uuid"),
    )
    op.add_column("peck", sa.Column("chicken_uuid", sa.String(), nullable=True))
    op.create_foreign_key(None, "peck", "chicken", ["chicken_uuid"], ["uuid"])


def downgrade():
    op.drop_constraint(None, "peck", type_="foreignkey")
    op.drop_column("peck", "chicken_uuid")
    op.drop_table("chicken")
    op.drop_table("brood")
