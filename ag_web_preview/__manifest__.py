###################################################################################
#
#    Copyright (c) 2017-2019 ag IT GmbH.
#
#    This file is part of ag Preview
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
    "name": "ag Preview",
    "summary": """File Preview Dialog""",
    "version": "12.0.3.0.2",
    "category": "Extra Tools",
    "license": "LGPL-3",
    "website": "http://www.agit.at",
    'live_test_url': 'https://agit.at/r/SgN',
    "author": "ag IT",
    "contributors": [
        "Mathias Markl <mathias.markl@agit.at>",
    ],
    "depends": [
        "ag_web_utils",
    ],
    "data": [
        "template/assets.xml",
        "views/res_config_settings_view.xml",
    ],
    "demo": [
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