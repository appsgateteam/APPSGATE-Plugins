###################################################################################
#
#    Copyright (c) 2017-2019 ag IT GmbH.
#
#    This file is part of ag Documents Large Object
#    (see https://agit.at).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.
#
###################################################################################

import os
import base64
import logging

from odoo.exceptions import AccessError, ValidationError

from odoo.addons.ag_utils.tests.common import multi_users
from odoo.addons.ag_dms.tests.common import setup_data_function
from odoo.addons.ag_dms.tests.test_file import FileTestCase

_path = os.path.dirname(os.path.dirname(__file__))
_logger = logging.getLogger(__name__)

class FileLObjectTestCase(FileTestCase):

    def _setup_test_data(self):
        super(FileLObjectTestCase, self)._setup_test_data()
        self.new_storage.write({'save_type': 'lobject'})
    
    @multi_users(lambda self: self.multi_users())
    @setup_data_function(setup_func='_setup_test_data')
    def test_content_lobject(self):
        storage = self.create_storage(save_type="lobject", sudo=True)
        lobject_file = self.create_file(storage=storage)
        self.assertTrue(lobject_file.content)
        self.assertTrue(lobject_file.content_lobject)
        self.assertTrue(lobject_file.with_context({'bin_size': True}).content)
        self.assertTrue(lobject_file.with_context({'bin_size': True}).content_lobject)
        self.assertTrue(lobject_file.with_context({'human_size': True}).content_lobject)
        self.assertTrue(lobject_file.with_context({'base64': True}).content_lobject)
        self.assertTrue(lobject_file.with_context({'stream': True}).content_lobject)
        oid = lobject_file.with_context({'oid': True}).content_lobject
        self.assertTrue(oid)
        lobject_file.write({'content': base64.b64encode(b"\xff content")})
        self.assertTrue(oid != lobject_file.with_context({'oid': True}).content_lobject)
        self.assertTrue(lobject_file.export_data(['content']))
        self.assertTrue(lobject_file.export_data(['content'], raw_data=True))
        lobject_file.unlink()