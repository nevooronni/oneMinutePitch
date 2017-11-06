"""added lines column to pitchlist

Revision ID: df2d3ab625cd
Revises: 3520b7c7182d
Create Date: 2017-11-04 18:04:20.303167

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'df2d3ab625cd'
down_revision = '3520b7c7182d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('content', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pitches', 'content')
    # ### end Alembic commands ###