# -*- coding: utf-8 -*-
{
    'name': 'WPS report for Qatar',
    'author': 'Almisned Technology',
    "license": "OPL-1",
    'website': 'https://www.misnedtech.com',
    'support': 'info@misnedtech.com',
    'version': '17.0',
    'category': 'Payroll',
    'summary': """WPS report""",
    'description': """WPS report in csv format
    """,
    'depends': ['hr_payroll',
                'hr_holidays'],
    'data': [
        'security/ir.model.access.csv',
        'security/wps_report.xml',
        'wizard/payroll_transfer_sheet_view.xml',
        'views/hr_payslip_views.xml',
        'views/res_partner_views.xml',
        'views/hr_contract_views.xml',
        'views/hr_employee_views.xml',
        'views/hr_leave_views.xml',
        'report/timeoff_report.xml',
        'report/timeoff_report_reg.xml',
    ],
    'images': ['static/description/background.png', ],
    'auto_install': False,
    'installable': True,
    'application': True,
    "price": 95,
    "currency": "EUR"
}
