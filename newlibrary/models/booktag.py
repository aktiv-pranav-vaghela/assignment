# - * - coding: utf - 8 -*-

from odoo import fields,models
class booktag(models.Model):
    _name="newlibrary.book.tags"
    _description='''
        This file shall have the book tags.
    '''
    name = fields.Char(string="Book Tag",required=True)

