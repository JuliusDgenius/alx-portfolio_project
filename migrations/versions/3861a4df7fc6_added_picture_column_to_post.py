"""added picture column to post

Revision ID: 3861a4df7fc6
Revises: e3344ee293b8
Create Date: 2024-09-19 11:00:30.349969

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3861a4df7fc6'
down_revision = 'e3344ee293b8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('post_image', sa.String(length=255), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_column('post_image')

    # ### end Alembic commands ###
