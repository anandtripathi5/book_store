"""fixed days and fixed charge introduced

Revision ID: 1f44aba213bf
Revises: 9b10f20a23c5
Create Date: 2018-05-17 09:21:46.210715

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from sqlalchemy.dialects import mysql

revision = '1f44aba213bf'
down_revision = '9b10f20a23c5'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        'book_type',
        sa.Column('fixed_days', mysql.INTEGER(display_width=11), nullable=False,
                  server_default=sa.text("0"))
    )
    op.add_column(
        'book_type',
        sa.Column('fixed_charges', mysql.DECIMAL(20, 6),
                  nullable=False,
                  server_default=sa.text("0"))
    )


def downgrade():
    op.drop_column('book_type', 'fixed_days')
    op.drop_column('book_type', 'fixed_charges')
