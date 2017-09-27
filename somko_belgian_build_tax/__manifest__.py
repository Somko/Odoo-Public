# -*- coding: utf-8 -*-
{
    'name': 'Belgian build tax',
    'version': '1.0',
    'author': 'Somko',
    'category': 'PGlas',
    'description': """""",
    'website': 'http://www.somko.be',
    'images': [],
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
