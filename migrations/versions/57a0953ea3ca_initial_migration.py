"""Initial migration

Revision ID: 57a0953ea3ca
Revises: 
Create Date: 2024-09-12 23:16:33.831088

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '57a0953ea3ca'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=60), nullable=False),
    sa.Column('profile_pic', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('benefit',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('benefit_image', sa.String(length=255), nullable=True),
    sa.Column('benefit_requirement', sa.Text(), nullable=True),
    sa.Column('benefit_link', sa.String(length=60), nullable=True),
    sa.Column('benefit_start_date', sa.DateTime(), nullable=False),
    sa.Column('benefit_end_date', sa.DateTime(), nullable=False),
    sa.Column('benefit_status', sa.String(length=60), nullable=False),
    sa.Column('benefit_created_by', sa.String(length=60), nullable=False),
    sa.Column('benefit_created_on', sa.DateTime(), nullable=False),
    sa.Column('benefit_updated_by', sa.String(length=60), nullable=False),
    sa.Column('benefit_updated_on', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=20), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('date_posted', sa.DateTime(), nullable=False),
    sa.Column('author', sa.String(length=60), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('content'),
    sa.UniqueConstraint('title')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post')
    op.drop_table('benefit')
    op.drop_table('user')
    # ### end Alembic commands ###
