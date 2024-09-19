"""Manual update requirement and description fields to Text

Revision ID: e3344ee293b8
Revises: 57a0953ea3ca
Create Date: 2024-09-19 00:08:26.221923

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e3344ee293b8'
down_revision = '57a0953ea3ca'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('benefit') as batch_op:
        batch_op.alter_column('description',
                    existing_type=sa.String(length=255),
                    type_=sa.Text(),
                    existing_nullable=False)
        batch_op.alter_column('benefit_requirement',
                    existing_type=sa.String(length=60),
                    type_=sa.Text(),
                    existing_nullable=True) 


def downgrade():
    pass
