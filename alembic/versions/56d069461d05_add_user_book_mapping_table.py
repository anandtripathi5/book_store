"""add user_book_mapping table

Revision ID: 56d069461d05
Revises: 87827af96ccd
Create Date: 2018-05-16 23:30:32.316480

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '56d069461d05'
down_revision = '87827af96ccd'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('user_book_mapping',
                    sa.Column('id', mysql.INTEGER(display_width=11),
                              nullable=False),
                    sa.Column('user_id', mysql.INTEGER(display_width=11),
                              autoincrement=False, nullable=False),
                    sa.Column('book_id', mysql.INTEGER(display_width=11),
                              autoincrement=False, nullable=False),
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
                    sa.ForeignKeyConstraint(['book_id'], [u'books.id'],
                                            name=u'user_book_mapping_ibfk_2'),
                    sa.ForeignKeyConstraint(['user_id'], [u'users.id'],
                                            name=u'user_book_mapping_ibfk_1'),
                    sa.PrimaryKeyConstraint('id'),
                    mysql_default_charset=u'latin1',
                    mysql_engine=u'InnoDB'
                    )
    op.create_index('user_id', 'user_book_mapping', ['user_id', 'book_id'],
                    unique=True)


def downgrade():
    op.drop_table('user_book_mapping')