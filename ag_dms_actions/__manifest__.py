###################################################################################
#
#    Copyright (c) 2017-2019 ag IT GmbH.
#
#    This file is part of ag Documents Actions
#    (see https://agit.at).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.
#
###################################################################################

{
    "name": "Documents Actions",
    "summary": """Custom File Operations""",
    "version": '12.0.2.0.1',   
    "category": 'Document Management',   
    "license": "LGPL-3",
    "author": "APPSGATE FZC LLC",

    "depends": [
        "ag_dms",
    ],
    "data": [
        "security/ir.model.access.csv",
        "template/assets.xml",
        "views/action.xml",
        "views/file.xml",
        "views/server_actions.xml",
        "views/res_config_settings.xml",
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
}