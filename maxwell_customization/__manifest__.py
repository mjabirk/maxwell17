# -*- coding: utf-8 -*-
{
    'name': 'Maxwell Customization',
    'author': 'Mohammed Jabir',
    "license": "OPL-1",
    'support': 'jabirodoo@gmail.com',
    'version': '17.0',
    'category': 'Misx',
    'summary': """SO and PO customization""",
    'description': """Option to hide sales order lines from customer
    Sales order report 
    Purchase order report
    """,
    'depends': ['sale',
                'purchase',
                'account',],
    'data': [
        'views/sale_order_line_views.xml',
        'views/sale_order_views.xml',
        'views/account_move_views.xml',
        'views/purchase_order_views.xml',
        'report/ir_actions_report_templates.xml',
        'report/purchase_order_templates.xml',
    ],
    'images': ['static/description/background.png', ],
    'auto_install': False,
    'installable': True,
    'application': True,
    "price": 395,
    "currency": "EUR"
}
