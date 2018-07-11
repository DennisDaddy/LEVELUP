"""empty message

Revision ID: 8336b18f7a14
Revises: e2e2449fb1d8
Create Date: 2018-07-11 14:11:47.754165

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8336b18f7a14'
down_revision = 'e2e2449fb1d8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('date_modified', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comments')
    # ### end Alembic commands ###
