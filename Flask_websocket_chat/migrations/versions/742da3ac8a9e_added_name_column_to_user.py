"""Added name column to User

Revision ID: 742da3ac8a9e
Revises: 
Create Date: 2024-03-22 18:47:19.142136

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '742da3ac8a9e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(length=64), nullable=True))
        batch_op.drop_index('ix_user_username')
        batch_op.create_index(batch_op.f('ix_user_name'), ['name'], unique=True)
        batch_op.drop_column('username')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('username', sa.VARCHAR(length=64), autoincrement=False, nullable=True))
        batch_op.drop_index(batch_op.f('ix_user_name'))
        batch_op.create_index('ix_user_username', ['username'], unique=True)
        batch_op.drop_column('name')

    # ### end Alembic commands ###
