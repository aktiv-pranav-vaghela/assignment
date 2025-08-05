{
    'name': 'ak_library_management',
    'version': '18.0.1.0.0',
    'author': 'Pranav',
    'category': 'Library',
    'website': 'https://www.aktivsoftware.com',
    'description': """
Library management.
""",
    'depends': ["base","web"],
    'data': [
        'security/ir.model.access.csv',
        'views/library_book_view.xml',
        'views/library_member_view.xml',
        'views/library_book_category_view.xml',
        'views/library_menu_action_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}