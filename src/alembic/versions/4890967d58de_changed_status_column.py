"""changed status column

Revision ID: 4890967d58de
Revises: 1b1d89319130
Create Date: 2024-11-27 14:41:26.296198

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "4890967d58de"
down_revision: Union[str, None] = "1b1d89319130"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

todostatus_enum = sa.Enum(
    "OPEN", "IN_PROGRESS", "DONE", "CLOSED", "CANCELLED", name="todostatus"
)


def upgrade() -> None:
    # Create the Enum type in the database
    todostatus_enum.create(op.get_bind())

    # Alter the column using explicit casting
    op.execute(
        """
        UPDATE todos
        SET status = CASE
            WHEN status = 'open' THEN 'OPEN'
            WHEN status = 'in_progress' THEN 'IN_PROGRESS'
            WHEN status = 'done' THEN 'DONE'
            WHEN status = 'closed' THEN 'CLOSED'
            WHEN status = 'cancelled' THEN 'CANCELLED'
            ELSE status
        END
        WHERE status IS NOT NULL;
        """
    )

    op.execute(
        """
        ALTER TABLE todos
        ALTER COLUMN status TYPE todostatus
        USING status::todostatus;
    """
    )

    # Create unique constraint
    op.create_unique_constraint("uq_todos_id", "todos", ["id"])


def downgrade() -> None:
    # Drop the unique constraint
    op.drop_constraint("uq_todos_id", "todos", type_="unique")

    # Revert the column type back to VARCHAR with explicit casting
    op.execute(
        """
        ALTER TABLE todos
        ALTER COLUMN status TYPE VARCHAR(25);
    """
    )

    # Drop the Enum type
    todostatus_enum.drop(op.get_bind())
