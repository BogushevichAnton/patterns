"""init note

Revision ID: ef6a0fcfa5a2
Revises: 2fc942af851e
Create Date: 2026-11-21 15:02:17.992111

"""

from collections.abc import Sequence

import sqlalchemy as sa

from alembic import op

revision: str = "ef6a0fcfa5a2"
down_revision: str | Sequence[str] | None = "2fc942af851e"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "note",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=50), nullable=False),
        sa.Column("description", sa.String(length=100), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_note")),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("note")
