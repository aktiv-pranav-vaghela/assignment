# - * - coding: utf - 8 -*-
{
    'name':'newlibrary',
    'description':'NewLibrary module',
    'version':'18.0.1.0.0',
    'license':'LGPL-3',
    'author':'Pranav',
    'category':'newlibrary',
    'data':[
        'security/ir.model.access.csv',
        'views/book_view.xml',
        'views/library_view.xml',
        'views/book_tags_view.xml',
        'views/book_category_view.xml',
        'views/library_menu.xml',
    ],
    'depends':['base'],
    'description':'''
        library data shall be stored.
    ''',
    'website':'www.library-site.com',
    'installable':True,
    'application':True,
    'auto_install':False,
}