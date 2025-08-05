# -*- coding: utf-8 -*-
from odoo import models, fields

#This class shall include the details of categories of books.
class BookCategory(models.Model):
    '''
       This class extends the models class.
    '''
    _name = "book.category"
    _description = "Library Book Management book.category"

    name = fields.Char(string="Add Book Category ", required=True)