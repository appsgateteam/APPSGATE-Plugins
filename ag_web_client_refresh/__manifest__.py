###################################################################################
#
#    Copyright (c) 2017-2019 ag IT GmbH.
#
#    This file is part of ag Web Refresh
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
    "name": "Web Refresh",
    "summary": """Web Client Refresh""",
    "version": "12.0.3.0.5",
    "category": "Extra Tools",
    "license": "AGPL-3",

    "author": "APPSGATE FZC LLC",

    "depends": [
        "base_automation",
        "ag_web_client",
    ],
    "data": [
        "template/assets.xml",
        "views/refresh_action_view.xml",
        "views/res_config_settings_view.xml",
        "data/refresh_actions.xml",
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
    "post_init_hook": "_install_initialize_rules",
    "uninstall_hook": "_uninstall_remove_rules",
}