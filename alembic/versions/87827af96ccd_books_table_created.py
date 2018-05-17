"""books table created

Revision ID: 87827af96ccd
Revises: 3be0cf06e60d
Create Date: 2018-05-16 22:55:24.257907

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from sqlalchemy.dialects import mysql

revision = '87827af96ccd'
down_revision = '3be0cf06e60d'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('books',
                    sa.Column('id', mysql.INTEGER(display_width=11),
                              nullable=False),
                    sa.Column('book_name', mysql.VARCHAR(length=128),
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


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('books')
    # ### end Alembic commands ###