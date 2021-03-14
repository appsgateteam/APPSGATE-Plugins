###################################################################################
#
#    Copyright (c) 2017-2019 ag IT GmbH.
#
#    This file is part of ag Documents Chatter
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

import base64
import logging

from odoo import models, api, fields

_logger = logging.getLogger(__name__)

class File(models.Model):
    
    _name = 'ag_dms.file'
    
    _inherit = [
        'mail.thread',
        'mail.activity.mixin',
        'ag_dms.file',
    ]
    
    #----------------------------------------------------------
    # Create / Update / Delete
    #----------------------------------------------------------
    
    @api.model_create_multi
    def create(self, vals_list):
        return super(File, self.with_context(mail_create_nolog=True)).create(vals_list)