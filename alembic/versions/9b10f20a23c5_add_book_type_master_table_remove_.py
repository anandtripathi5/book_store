"""add book type master table remove charges column

Revision ID: 9b10f20a23c5
Revises: 1792430b5062
Create Date: 2018-05-17 08:42:18.453496

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from sqlalchemy.dialects import mysql

revision = '9b10f20a23c5'
down_revision = '1792430b5062'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('book_type',
                    sa.Column('id', mysql.INTEGER(display_width=11),
                              nullable=False),
                    sa.Column('book_type', mysql.VARCHAR(length=126),
                              nullable=False),
                    sa.Column('charge', mysql.DECIMAL(20, 6),
                              nullable=False),
                    sa.Column('created_on', mysql.DATETIME(),
                              server_default=sa.text(u'CURRENT_TIMESTAMP'),
                              nullable=True),
                    sa.Column('modified_on', mysql.TIMESTAMP(),
                              server_default=sa.text(
                                  u'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),
                              nullable=False),
                    sa.Column('is_deleted', mysql.TINYINT(display_width=1),
                              server_default=sa.text(u"'0'"),
                              autoincrement=False, nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    mysql_default_charset=u'latin1',
                    mysql_engine=u'InnoDB'
                    )
    op.add_column(
        'books',
        sa.Column('book_type_id', mysql.INTEGER(display_width=11), nullable=False)
    )
    op.drop_column('books', 'charge')
    op.create_foreign_key(
        'fk_book_type_id',
        'books', 'book_type',
        ['book_type_id'], ['id'],
    )


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('books', 'book_type_id')
    op.add_column(
        'books',
        sa.Column('charge', mysql.INTEGER(display_width=11), nullable=False,
                  server_default=sa.text("1"))
    )
    op.drop_table('book_type')
    # ### end Alembic commands ###
