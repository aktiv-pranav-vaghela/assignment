# - * - coding: utf - 8 -*-
{
    'name':'library',
    'description':'Library module',
    'version':'18.0.1.0.0',
    'license':'LGPL3',
    'author':'Pranav',
    'category':'library',
    'data':[
        'security/ir.model.access.csv',
        'views/book_view.xml',
        'views/library_view.xml',
        'views/library_menu.xml',
    ],
    'depends':['base'],
    'description':'''
        library data shall be stored.
    ''',
    'website':'www.library-site.com',
    'installable':True,
    'applicatin':True,
    'auto_install':False,
}