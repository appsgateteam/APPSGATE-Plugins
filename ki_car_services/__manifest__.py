# -*- coding: utf-8 -*-
# Part of Kiran Infosoft. See LICENSE file for full copyright and licensing details.
{
    'name': "Car Service Booking Management",
    'summary': """ Car Service Booking Management """,
    'description': """
Car Service Booking Management
==================================
Car Service Booking
vehicle
service
maintenance
vehicle service
appointment
""",
    "version": "1.0",
    "category": "Human Resources",
    # 'author': "Kiran Infosoft",
    # "website": "http://www.kiraninfosoft.com",
    'license': 'Other proprietary',
    'price': 82.0,
    'currency': 'EUR',
    'images': ['static/description/image.jpg'],
    "depends": [
        'fleet',
        'sale_timesheet',
        'website_sale',
    ],
    "data": [
        'data/website_menu.xml',
        'security/ir.model.access.csv',
        'data/slot_data.xml',
        'views/slot_view.xml',
        'views/product_view.xml',
        'views/sale_view.xml',
        'views/project_view.xml',
        'views/website_template.xml',
        'views/report_sale.xml',
        'views/report_service.xml',
        'views/vehicle_view.xml',
        'views/menu.xml'
    ],
    "application": False,
    'installable': True,
}
