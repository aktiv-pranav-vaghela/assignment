# -*- coding: utf-8 -*-
from odoo import models, fields

#This class shall include the details of Books.
class LibraryBook(models.Model):
    '''
    This class extends the models class.
    '''
    _name = 'library.book'
    _discription  = '''
    library.book: Stores information related to books.
    '''

    name = fields.Char(string="Book Title",required=True)
    author = fields.Char(string="Author Name")
    isbn = fields.Char(string="ISBN Number",required = True)
    publication_date = fields.Date(string="Date of Publication",required = True)
    category_id = fields.Many2one('book.category', string='Category')
    state = fields.Selection([('available','Available'),('borrowed','Borrowed')],required = True)
    description = fields.Text(string='Description')