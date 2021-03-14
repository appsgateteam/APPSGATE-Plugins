###################################################################################
#
#    Copyright (c) 2017-2019 ag IT GmbH.
#
#    This file is part of ag Documents Thumbnails
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

{
    "name": 'Documents Thumbnails',
    "summary": """Automatic File Thumbnails""", 
    "version": '12.0.2.0.0',   
    "category": 'Document Management',   
    "license": "LGPL-3",
    "author": "APPSGATE FZC LLC",

    "depends": [
        'ag_dms',
    ],
    "data": [
        "views/storage.xml",
        "views/res_config_settings.xml",
        "data/ir_cron.xml",
    ],
    "demo": [
    ],
    "qweb": [
        "static/src/xml/*.xml",
    ],
    "images": [
        'static/description/banner.png'
    ],
    "application": False,
    "installable": True,
}
