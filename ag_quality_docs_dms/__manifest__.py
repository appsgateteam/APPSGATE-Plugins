###################################################################################
#
#    Copyright (c) 2017-2019 ag IT GmbH.
#
#    This file is part of ag QMS Documents DMS Support
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
    "name": "QMS Documents DMS Support",
    "summary": """Quality Management System DMS Support""",
    "version": "12.0.2.0.1",
    "author": "APPSGATE FZC LLC",
    "category": "Document Management",
    "license": "LGPL-3",

    "depends": [
        "ag_quality_docs",
        "ag_dms_field",
        "ag_web_preview",
    ],

    "data": [
        "template/assets.xml",
        "views/document_view.xml",
        "views/template_view.xml",
        "views/res_config_view.xml",
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
    "installable": True,
    "auto_install": False,
    "application": False,
}
