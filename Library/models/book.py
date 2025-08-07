# - * - coding: utf - 8 -*-
from odoo import models, fields,api

#This model shall contain information related to books.
class Book(models.Model):
    _name = 'library.book'
    _description = """ This class shall hold information related to book. """

    name = fields.Char(string='Book Title', required=True)
    author = fields.Char(string='Author')
    isbn = fields.Char(string='ISBN')
    # Many2one relationship to library
    library_id = fields.Many2one('library.library', string='Library')

    # relation fields to fetch Many2many relation to location on library.library class
    library_location = fields.Char(string="Library Location", related="library_id.location")
    #Book_reference apply onchange method in view side
    book_reference = fields.Char(string="Book Reference", onchange="_onchange_book_reference")

    #This method shall merge title and author name.
    @api.onchange("name", "author")
    def _onchange_book_reference(self):
        self.book_reference = str(self.name) + "-" + str(self.author)

