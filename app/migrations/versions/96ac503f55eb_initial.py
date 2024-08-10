"""initial

Revision ID: 96ac503f55eb
Revises: 093df1bbebfc
Create Date: 2024-08-10 17:27:01.451344

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '96ac503f55eb'
down_revision: Union[str, None] = '093df1bbebfc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'notifications', ['user_id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'notifications', type_='unique')
    # ### end Alembic commands ###
