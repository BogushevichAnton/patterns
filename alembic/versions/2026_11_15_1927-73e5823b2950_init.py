"""init.

Revision ID: 73e5823b2950
Revises:
Create Date: 2026-11-15 19:27:43.347878

"""

from collections.abc import Sequence

revision: str = "73e5823b2950"
down_revision: str | Sequence[str] | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
