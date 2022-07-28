"""create words table

Revision ID: 14470aef53a1
Revises: 
Create Date: 2022-07-13 10:19:14.087747

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '14470aef53a1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'notes',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String(250), nullable=False),
        sa.Column('color', sa.String(10)),
        sa.Column('text', sa.Text),
    )


def downgrade() -> None:
    op.drop_table('notes')
