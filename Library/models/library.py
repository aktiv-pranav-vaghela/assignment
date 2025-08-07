# - * - coding: utf - 8 -*-
from odoo import models, fields

#This model shall contain the information of library.
class Library(models.Model):
    _name = 'library.library'
    _description = """ This class shall hold library information and multiple books can be in the same library. """

    name = fields.Char(string='Library Name', required=True)
    location = fields.Char(string='Location')
    capacity = fields.Integer(string='Capacity')
    notes = fields.Text(string='Notes')
    #One2many relationship of library with books.
    book_ids = fields.One2many('library.book', 'library_id', string='Books')


