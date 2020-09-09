# -*- coding: utf-8 -*-
# Part of Sananaz Mansuri See LICENSE file for full copyright and licensing details.

{
    'name': "Equipment Extend Custom",
    'version': '1.1.1',
    'category': 'Field Service',
    'license': 'Other proprietary',
    'currency': 'EUR',
    'summary':  """Added Warranty Details on Field Service Equipment.
""",
    'description': """
Added Warranty Details on Field Service Equipment.

    """,
    'author': 'Sananaz Mansuri',
    'website': 'http://www.odoo.com',
    # 'images': ['static/description/IMG.png'],
    'depends': [
                'fieldservice',
                ],
    'data': [
      'views/fsm_equipment.xml'  
    ],
    'installable': True,
    'application': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
