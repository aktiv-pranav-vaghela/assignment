# - * - coding: utf - 8 -*-

from odoo import fields,models

class bookcategory(models.Model):
    _name="newlibrary.book.category"
    _description='''
        This class shall contain the details of book category.
    '''

    name=fields.Char(string="Book Category",required=True)
    tag_ids=fields.Many2many("newlibrary.book.tags",string="Book Tags")

