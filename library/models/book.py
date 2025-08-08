# - * - coding: utf - 8 -*-
from odoo import models, fields

#This model shall contain information related to books.
class Book(models.Model):
    _name = 'library.book'
    _description = """ This class shall hold information related to book. """

    name = fields.Char(string='Book Title', required=True)
    author = fields.Char(string='Author')
    isbn = fields.Char(string='ISBN')
    # Many2one relationship to library
    library_id = fields.Many2one('library.library', string='Library')

