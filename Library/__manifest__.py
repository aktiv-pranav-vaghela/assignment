# - * - coding: utf - 8 -*-
{
    'name': 'lat_Library',
    'version': '18.0.1.0.0',
    'author': 'Pranav',
    'category': 'Library',
    'website': 'https://www.aktivsoftware.com',
    'description': """Library management between books and library using One2many and Many2one relationship""",
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'views/library_view.xml',
        'views/book_view.xml',
        'views/library_menu_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
