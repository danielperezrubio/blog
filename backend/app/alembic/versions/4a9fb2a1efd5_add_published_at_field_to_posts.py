"""Add published_at field to posts

Revision ID: 4a9fb2a1efd5
Revises: ecbd49d3303b
Create Date: 2023-11-25 09:12:12.806876

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4a9fb2a1efd5'
down_revision: Union[str, None] = 'ecbd49d3303b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('published_at', sa.DateTime(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'published_at')
    # ### end Alembic commands ###
