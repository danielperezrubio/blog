"""Add updated_at field to posts

Revision ID: a64d4fafc7f4
Revises: 4a9fb2a1efd5
Create Date: 2023-11-25 09:17:23.570679

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a64d4fafc7f4'
down_revision: Union[str, None] = '4a9fb2a1efd5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('updated_at', sa.DateTime(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'updated_at')
    # ### end Alembic commands ###
