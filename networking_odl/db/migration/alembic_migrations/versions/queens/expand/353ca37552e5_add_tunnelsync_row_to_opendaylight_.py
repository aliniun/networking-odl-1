# Copyright 2015 OpenStack Foundation
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#

"""add tunnelsync row to opendaylight preiodic task table

Revision ID: 353ca37552e5
Revises: 6f7dfb241354
Create Date: 2019-06-12 03:04:03.007838

"""

# revision identifiers, used by Alembic.
revision = '353ca37552e5'
down_revision = '6f7dfb241354'

from alembic import op
from sqlalchemy.sql import column, table
import sqlalchemy as sa

from networking_odl.common import constants as odl_const


def upgrade():
    periodic_table = table('opendaylight_periodic_task',
        column('task', sa.String(70)),
        column('state', sa.Enum)
    )
    op.bulk_insert(periodic_table,
                    [{'task': 'tunnelsync',
                      'state': odl_const.PENDING}])