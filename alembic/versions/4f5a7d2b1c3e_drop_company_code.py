"""drop company_code from companies

Revision ID: 4f5a7d2b1c3e
Revises: e8907e5318dc
Create Date: 2026-06-21 00:00:00.000000
"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "4f5a7d2b1c3e"
down_revision: Union[str, Sequence[str], None] = "e8907e5318dc"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.drop_index(op.f("ix_companies_company_code"), table_name="companies")
    op.drop_column("companies", "company_code")


def downgrade() -> None:
    """Downgrade schema."""
    op.add_column(
        "companies",
        sa.Column("company_code", sa.String(), nullable=True),
    )
    op.create_index(
        op.f("ix_companies_company_code"),
        "companies",
        ["company_code"],
        unique=True,
    )
