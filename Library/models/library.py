# - * - coding: utf - 8 -*-
from odoo import models, fields,api

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

    #This field shall show the count of books.
    book_count = fields.Integer(string='Book Count', compute="_compute_book_count")
    # This field shall indicate the capacity status between book_count and capacity.
    capacity_status = fields.Char(string='Capacity Status', compute="_compute_capacity_status", default="0%")

    # find a related book count
    @api.depends("book_ids")
    def _compute_book_count(self):
        for record in self:
            record.book_count = len(record.book_ids)

    # use "book_count","capacity" to make capacity status
    @api.depends("book_count", "capacity")
    def _compute_capacity_status(self):
        for record in self:
            try:
                percentage = int((record.book_count * 100) / record.capacity)
                if percentage < 80:
                    record.capacity_status = "Normal"
                elif 80 <= percentage < 100:
                    record.capacity_status = "Warning"
                else:
                    record.capacity_status = "Full"
            except:
                record.capacity_status = "Capacity is 0"

