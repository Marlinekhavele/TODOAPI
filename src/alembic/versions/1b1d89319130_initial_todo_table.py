"""Initial todo  table

Revision ID: 1b1d89319130
Revises:
Create Date: 2024-11-27 12:16:56.471594

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "1b1d89319130"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "todos",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("description", sa.String(length=200), nullable=True),
        sa.Column("status", sa.String(length=25), nullable=True),
        sa.PrimaryKeyConstraint("id", name="todo_pk"),
        sa.UniqueConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("todos")
    # ### end Alembic commands ###
