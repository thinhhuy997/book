"""add_new_column1_to_book

Revision ID: 1fb027d50b2f
Revises: 19f762069491
Create Date: 2023-12-13 00:53:30.342620

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1fb027d50b2f'
down_revision: Union[str, None] = '19f762069491'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('books', sa.Column('author2', sa.String()))  # Thêm cột mới


def downgrade() -> None:
    pass
