"""add2_foreign_key

Revision ID: 7c5b0bf594f1
Revises: 1639f51798cb
Create Date: 2023-12-14 00:18:06.619222

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7c5b0bf594f1'
down_revision: Union[str, None] = '1639f51798cb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
        op.add_column('books', sa.Column('authors', sa.Integer, sa.ForeignKey('author.id')))



def downgrade() -> None:
    pass
