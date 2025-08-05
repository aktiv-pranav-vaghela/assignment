# - * - coding: utf - 8 -*-
from odoo import models,fields

class Book(models.Model):
    _name = 'libr.book'
    _description = '''
        This class shall have the information of books.
'''
    name = fields.Char(string = "Book Name",required = True)
    author = fields.Char(string = "Book author",required = True)
    isbn = fields.Char(string = "ISBN",required = True)

    # Implements many2one relationship with library
    library_id = fields.Many2one('libr.library',string = "Library")