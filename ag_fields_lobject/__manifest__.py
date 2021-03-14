###################################################################################
#
#    Copyright (c) 2017-2019 ag IT GmbH.
#
#    This file is part of ag Large Objects Field
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
    "name": "Large Objects Field",
    "summary": """PGSQL Large Objects Support for Fields""",
    "version": '12.0.3.0.1',   
    "category": 'Extra Tools',   
    "license": "LGPL-3",
    "author": "APPSGATE FZC LLC",

    "depends": [
        "ag_utils",
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
    "auto_install": False,
    "application": False,
    "installable": True,
    "post_load": "_patch_system",
}
