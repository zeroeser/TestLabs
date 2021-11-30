"""Change something

Revision ID: f26af09b829f
Revises: af1ea6854190
Create Date: 2021-11-30 12:20:33.914186

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f26af09b829f'
down_revision = 'af1ea6854190'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('users', 'surname',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'surname',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('users', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###