"""empty message

Revision ID: 6098e9ec6637
Revises: ef4f2d38dd8f
Create Date: 2021-04-03 19:40:11.587643

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6098e9ec6637'
down_revision = 'ef4f2d38dd8f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('userid', sa.Integer(), nullable=True))
    op.drop_constraint('products_parent_id_fkey', 'products', type_='foreignkey')
    op.create_foreign_key(None, 'products', 'users', ['userid'], ['id'])
    op.drop_column('products', 'parent_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('parent_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'products', type_='foreignkey')
    op.create_foreign_key('products_parent_id_fkey', 'products', 'users', ['parent_id'], ['id'])
    op.drop_column('products', 'userid')
    # ### end Alembic commands ###
