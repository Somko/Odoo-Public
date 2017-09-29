# -*- coding: utf-8 -*-
{
    'name': 'Renovation Tax Belgium',
    'version': '10.0.1',
    'author': 'Somko',
    'category': 'Accounting',
    'description': """
        Change the VAT tax with one mouse click from 21% to 6%.
        Print VAT certificates
        """,
    'website': 'https://www.somko.be',
    'images': ['static/description/module-cover.png',],
    'depends': ['account', 'sale', 'l10n_be'],
    'data': [
        'data/account_tax_template_data.xml',
        'data/fiscal_templates_data.xml',

        'views/invoice_form.xml',

        'report/report.xml',
    ],
    'qweb': [],
    'demo': [],
    'test': [],
    "auto_install": False,
    'application': False,
    "installable": True,
}
