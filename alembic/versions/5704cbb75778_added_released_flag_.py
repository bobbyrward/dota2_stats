"""Added released flag to heroes to block skywrath and such

Revision ID: 5704cbb75778
Revises: 2f5f82e2bb08
Create Date: 2013-02-07 19:16:27.922779

"""

# revision identifiers, used by Alembic.
revision = '5704cbb75778'
down_revision = '2f5f82e2bb08'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('hero', sa.Column('released', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('hero', 'released')
    ### end Alembic commands ###
