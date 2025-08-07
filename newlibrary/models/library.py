# - * - coding: utf - 8 -*-
from odoo import fields,models

#This class have the information about Library.
class Library(models.Model):
    '''
    This class extends the models class.
    '''
    _name='newlibrary.library'
    _description='''
        This class shall have the information of library.
'''

    name=fields.Char(string="Library name",required=True)
    location=fields.Char(string="Location")
    capacity=fields.Char(string="Capacity")
    notes=fields.Char(string="Notes")

    # Implements one2many relationship with book.
    book_ids=fields.One2many('newlibrary.book','library_id',string="Book ids")

