"""add_new_column_not_nullable

Revision ID: 6eb5aa370759
Revises: 1fb027d50b2f
Create Date: 2023-12-13 01:49:40.296579

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6eb5aa370759'
down_revision: Union[str, None] = '1fb027d50b2f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
  
    op.add_column('books', sa.Column('price', sa.Integer))

def downgrade():
    # Rollback (có thể không cần thiết tùy vào yêu cầu cụ thể)
    op.drop_column('books', 'price')
