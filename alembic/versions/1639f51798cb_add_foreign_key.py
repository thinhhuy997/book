"""add_foreign_key

Revision ID: 1639f51798cb
Revises: bd3e28ebc598
Create Date: 2023-12-14 00:16:38.040600

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1639f51798cb'
down_revision: Union[str, None] = 'bd3e28ebc598'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('books', sa.Column('author_id', sa.Integer, sa.ForeignKey('authors.id')))


def downgrade() -> None:
    pass
