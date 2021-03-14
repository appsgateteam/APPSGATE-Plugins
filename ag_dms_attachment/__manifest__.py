###################################################################################
#
#    Copyright (c) 2017-2019 ag IT GmbH.
#
#    This file is part of ag Documents Attachment
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
    "name": "Documents Attachment",
    "summary": """Documents as Attachment Storage""",
    "version": '12.0.3.0.7',   
    "category": 'Document Management',   
    "license": "LGPL-3",
    "author": "APPSGATE FZC LLC",

    'depends': [
        "ag_dms_actions",
    ],
    "data": [
        "views/menu.xml",
        "views/file.xml",
        "views/ir_attachment.xml",
        "views/res_config_settings.xml",
        "views/action.xml",
    ],
    "demo": [
        "demo/action.xml",
    ],
    "qweb": [
        "static/src/xml/*.xml",
    ],
    "images": [
        'static/description/banner.png'
    ],
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "application": False,
    "installable": True,
    "uninstall_hook": "_uninstall_force_storage",
}
