"""database done

Revision ID: b3822725bb23
Revises: f93a23fe3d39
Create Date: 2024-06-09 14:03:12.781640

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b3822725bb23'
down_revision: Union[str, None] = 'f93a23fe3d39'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('auth_tokens', sa.Column('usrname', sa.String(), nullable=True))
    op.create_index(op.f('ix_auth_tokens_usrname'), 'auth_tokens', ['usrname'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_auth_tokens_usrname'), table_name='auth_tokens')
    op.drop_column('auth_tokens', 'usrname')
    # ### end Alembic commands ###