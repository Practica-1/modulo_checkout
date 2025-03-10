{
    'name': 'Custom Checkout',
    'version': '1.0',
    'summary': 'Personaliza el formulario de checkout en Odoo 17',
    'category': 'Website',
    'author': 'Nicolas',
    'depends': ['website_sale'],
    'data': [
        'views/custom_checkout_view.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'static/src/js/checkout_form.js',
        ],
    },
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
    'demo': [],
}
