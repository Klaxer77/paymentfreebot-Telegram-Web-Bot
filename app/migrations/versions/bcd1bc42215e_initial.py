"""initial

Revision ID: bcd1bc42215e
Revises: 25c14f1c43ab
Create Date: 2024-07-30 21:45:35.944765

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bcd1bc42215e'
down_revision: Union[str, None] = '25c14f1c43ab'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('payment_history', sa.Column('user_id', sa.UUID(), nullable=False))
    op.create_foreign_key(None, 'payment_history', 'users', ['user_id'], ['id'])
    op.add_column('transactions', sa.Column('initiator', sa.UUID(), nullable=False))
    op.add_column('transactions', sa.Column('user_for', sa.UUID(), nullable=False))
    op.create_foreign_key(None, 'transactions', 'users', ['user_for'], ['id'])
    op.create_foreign_key(None, 'transactions', 'users', ['initiator'], ['id'])
    op.create_unique_constraint(None, 'users', ['chat_id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_constraint(None, 'transactions', type_='foreignkey')
    op.drop_constraint(None, 'transactions', type_='foreignkey')
    op.drop_column('transactions', 'user_for')
    op.drop_column('transactions', 'initiator')
    op.drop_constraint(None, 'payment_history', type_='foreignkey')
    op.drop_column('payment_history', 'user_id')
    # ### end Alembic commands ###
