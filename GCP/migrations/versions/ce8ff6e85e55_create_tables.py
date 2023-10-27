"""create tables

Revision ID: ce8ff6e85e55
Revises: 
Create Date: 2023-10-27 19:41:37.594512

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'ce8ff6e85e55'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('doctor_demographics')
    op.drop_index('MRN', table_name='patients')
    op.drop_table('patients')
    op.drop_index('patient_id', table_name='demographics')
    op.drop_table('demographics')
    op.add_column('doctor', sa.Column('NPI', sa.String(length=50), nullable=False))
    op.add_column('doctor', sa.Column('department', sa.String(length=50), nullable=False))
    op.add_column('doctor', sa.Column('first_name', sa.String(length=50), nullable=False))
    op.add_column('doctor', sa.Column('last_name', sa.String(length=50), nullable=False))
    op.drop_column('doctor', 'specialty')
    op.drop_column('doctor', 'MRN')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('doctor', sa.Column('MRN', mysql.VARCHAR(length=50), nullable=False))
    op.add_column('doctor', sa.Column('specialty', mysql.VARCHAR(length=50), nullable=False))
    op.drop_column('doctor', 'last_name')
    op.drop_column('doctor', 'first_name')
    op.drop_column('doctor', 'department')
    op.drop_column('doctor', 'NPI')
    op.create_table('demographics',
    sa.Column('demographic_id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('patient_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('first_name', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('last_name', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('date_of_birth', sa.DATE(), nullable=True),
    sa.Column('address', mysql.TEXT(), nullable=True),
    sa.Column('phone_number', mysql.VARCHAR(length=15), nullable=True),
    sa.Column('email', mysql.VARCHAR(length=100), nullable=True),
    sa.ForeignKeyConstraint(['patient_id'], ['patients.patient_id'], name='demographics_ibfk_1'),
    sa.PrimaryKeyConstraint('demographic_id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('patient_id', 'demographics', ['patient_id'], unique=False)
    op.create_table('patients',
    sa.Column('patient_id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('MRN', mysql.VARCHAR(length=50), nullable=False),
    sa.PrimaryKeyConstraint('patient_id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('MRN', 'patients', ['MRN'], unique=False)
    op.create_table('doctor_demographics',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('doctor_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('first_name', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('last_name', mysql.VARCHAR(length=50), nullable=False),
    sa.ForeignKeyConstraint(['doctor_id'], ['doctor.id'], name='doctor_demographics_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###