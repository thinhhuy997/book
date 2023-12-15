"""alter_price_column

Revision ID: bd3e28ebc598
Revises: 97f051fb9357
Create Date: 2023-12-13 01:54:37.043293

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bd3e28ebc598'
down_revision: Union[str, None] = '97f051fb9357'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('books', 'price', nullable=False)


def downgrade() -> None:
    pass
