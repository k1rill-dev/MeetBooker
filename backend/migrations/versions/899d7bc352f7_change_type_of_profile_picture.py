"""change type of profile picture

Revision ID: 899d7bc352f7
Revises: 086bbfc76c56
Create Date: 2024-05-29 17:27:39.061651

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '899d7bc352f7'
down_revision: Union[str, None] = '086bbfc76c56'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'profile_picture',
               existing_type=sa.BOOLEAN(),
               type_=sa.String(),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'profile_picture',
               existing_type=sa.String(),
               type_=sa.BOOLEAN(),
               existing_nullable=True)
    # ### end Alembic commands ###
