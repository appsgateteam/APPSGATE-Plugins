###################################################################################
#
#    Copyright (c) 2017-2019 ag IT GmbH.
#
#    This file is part of ag Autovacuum
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
    'name': 'Autovacuum',
    'summary': 'Configure automatic garbage collection',
    'version': '12.0.3.0.1',
    'category': 'Extra Tools',
    'license': 'LGPL-3',
    'author': 'APPSGATE FZC LLC',

    'depends': [
        'ag_utils',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/rules.xml',
        'data/rules.xml',
    ],
    'qweb': [
        'static/src/xml/*.xml',
    ],
    'images': [
        'static/description/banner.png'
    ],
    'external_dependencies': {
        'python': [],
        'bin': [],
    },
    'application': False,
    'installable': True,
    'auto_install': False,
}