"""init.

Revision ID: 2fc942af851e
Revises:
Create Date: 2026-11-15 19:34:25.677269

"""

from collections.abc import Sequence

revision: str = "2fc942af851e"
down_revision: str | Sequence[str] | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
