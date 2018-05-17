"""add column charge in books table

Revision ID: 1792430b5062
Revises: 56d069461d05
Create Date: 2018-05-17 07:56:47.529164

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from sqlalchemy.dialects import mysql

revision = '1792430b5062'
down_revision = '56d069461d05'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        'books',
        sa.Column('charge', mysql.INTEGER(display_width=11), nullable=False,
                  server_default=sa.text("1"))
    )


def downgrade():
    op.drop_column('books', 'charge')

