# -*- coding: utf-8 -*-
{
    'name': "Partner Working Calendar | Customer Working Hours | Vendor Working Days | Partner Business Hours | Schedule Calendar | Partner Availability Calendar",
    'version': '19.0.1.0.0',
    'category': 'Sales',
    'summary': 'Manage working schedules for partners with resource calendar integration.',
    'description': """
Partner Working Calendar
========================
This module allows you to define and manage working schedules for your partners (e.g., companies, depots, etc.) by integrating with Odoo's resource calendar. It enables you to configure operating hours, break times, and holidays for each partner address, making it easy to:
* Define working schedules for partners and their locations.
* Display opening hours or holidays on websites or reports.
* Integrate working schedules into other business logic, such as scheduling, VRP (Vehicle Routing Problem), etc.

Key Features:
* Assign working calendars to partner addresses.
* Flexible working schedules with support for multi-day weeks, breaks, and holidays.
* Automatic time zone management for accurate scheduling and display.
* Compatible with other modules using resource.calendar.
""",
    'website': 'https://uncannycs.com',
    'author': 'Uncanny Consulting Services LLP',
    'maintainer': 'Uncanny Consulting Services LLP',
    "license": 'Other proprietary',
    'depends': ['resource', 'mail', 'contacts'],
    'data': [
        'views/res_partner_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    "images": ['static/description/banner.gif'],
    "price": 25,
    "currency": "USD"
}
