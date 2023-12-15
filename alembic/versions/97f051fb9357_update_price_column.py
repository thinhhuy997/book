"""update_price_column

Revision ID: 97f051fb9357
Revises: 6eb5aa370759
Create Date: 2023-12-13 01:52:58.548500

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '97f051fb9357'
down_revision: Union[str, None] = '6eb5aa370759'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("UPDATE books SET price = 0 WHERE price IS NULL")



def downgrade() -> None:
    pass
