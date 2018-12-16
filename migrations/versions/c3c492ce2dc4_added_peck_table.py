"""Added peck table

Revision ID: c3c492ce2dc4
Revises: 
Create Date: 2018-12-16 21:24:50.501623

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "c3c492ce2dc4"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "peck",
        sa.Column("uuid", sa.String(length=36), nullable=False),
        sa.Column("created", sa.DateTime(), nullable=False),
        sa.Column("latitude", sa.Float(), nullable=False),
        sa.Column("longitude", sa.Float(), nullable=False),
        sa.Column("status", sa.String(length=1), nullable=False),
        sa.PrimaryKeyConstraint("uuid"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("peck")
    # ### end Alembic commands ###
