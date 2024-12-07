"""initial

Revision ID: 6068fc38e871
Revises: 
Create Date: 2024-12-07 15:08:04.592257

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6068fc38e871'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('chat_id', sa.Integer(), nullable=False),
    sa.Column('rating', sa.Float(), nullable=False),
    sa.Column('first_name', sa.String(length=255), nullable=False),
    sa.Column('last_name', sa.String(length=255), nullable=True),
    sa.Column('username', sa.String(length=255), nullable=False),
    sa.Column('balance', sa.DECIMAL(precision=10, scale=2), nullable=False),
    sa.Column('frozen_balance', sa.DECIMAL(precision=10, scale=2), nullable=False),
    sa.Column('is_premium', sa.Boolean(), nullable=True),
    sa.Column('register_date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('chat_id')
    )
    op.create_table('notifications',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.UUID(), nullable=False),
    sa.Column('create', sa.Boolean(), nullable=False),
    sa.Column('canceled', sa.Boolean(), nullable=False),
    sa.Column('accept', sa.Boolean(), nullable=False),
    sa.Column('conditions_are_met', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id')
    )
    op.create_table('payment_history',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('user_id', sa.UUID(), nullable=False),
    sa.Column('amount', sa.DECIMAL(precision=10, scale=2), nullable=False),
    sa.Column('last4', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('action', sa.String(length=255), nullable=False),
    sa.Column('status', sa.String(length=255), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_payment_history_user_id'), 'payment_history', ['user_id'], unique=False)
    op.create_table('ratings',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('rated_user_id', sa.UUID(), nullable=False),
    sa.Column('score', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['rated_user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_ratings_rated_user_id'), 'ratings', ['rated_user_id'], unique=False)
    op.create_table('transactions',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('initiator', sa.UUID(), nullable=False),
    sa.Column('user_for', sa.UUID(), nullable=False),
    sa.Column('sum', sa.DECIMAL(precision=10, scale=2), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('finished_at', sa.DateTime(), nullable=True),
    sa.Column('status', sa.String(length=255), nullable=False),
    sa.Column('creator', sa.UUID(), nullable=False),
    sa.ForeignKeyConstraint(['creator'], ['users.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['initiator'], ['users.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_for'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_transactions_initiator'), 'transactions', ['initiator'], unique=False)
    op.create_index(op.f('ix_transactions_user_for'), 'transactions', ['user_for'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_transactions_user_for'), table_name='transactions')
    op.drop_index(op.f('ix_transactions_initiator'), table_name='transactions')
    op.drop_table('transactions')
    op.drop_index(op.f('ix_ratings_rated_user_id'), table_name='ratings')
    op.drop_table('ratings')
    op.drop_index(op.f('ix_payment_history_user_id'), table_name='payment_history')
    op.drop_table('payment_history')
    op.drop_table('notifications')
    op.drop_table('users')
    # ### end Alembic commands ###