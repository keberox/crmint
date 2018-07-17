# Copyright 2018 Google Inc
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Create jobs

Revision ID: cd6376dcdf27
Revises: 94039d1c8c45
Create Date: 2017-04-24 16:52:47.535529

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd6376dcdf27'
down_revision = '94039d1c8c45'
branch_labels = None
depends_on = None


def upgrade():
  # ### commands auto generated by Alembic - please adjust! ###
  op.create_table('jobs',
  sa.Column('created_at', sa.DateTime(), nullable=False),
  sa.Column('updated_at', sa.DateTime(), nullable=False),
  sa.Column('id', sa.Integer(), nullable=False),
  sa.Column('name', sa.String(length=255), nullable=True),
  sa.Column('worker_class', sa.String(length=255), nullable=True),
  sa.Column('status', sa.String(length=50), nullable=False),
  sa.Column('status_changed_at', sa.DateTime(), nullable=True),
  sa.Column('pipeline_id', sa.Integer(), nullable=True),
  sa.ForeignKeyConstraint(['pipeline_id'], ['pipelines.id'], ),
  sa.PrimaryKeyConstraint('id')
  )
  # ### end Alembic commands ###


def downgrade():
  # ### commands auto generated by Alembic - please adjust! ###
  op.drop_table('jobs')
  # ### end Alembic commands ###