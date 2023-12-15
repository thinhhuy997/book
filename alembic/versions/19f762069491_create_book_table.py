"""create_book_table

Revision ID: 19f762069491
Revises: 
Create Date: 2023-12-13 00:47:34.148506

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '19f762069491'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('books', sa.Column('author', sa.String()))  # Thêm cột mới



def downgrade() -> None:
    pass
