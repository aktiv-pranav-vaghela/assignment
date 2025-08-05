# -*- coding: utf-8 -*-
from odoo import models,fields

#This class shall include the details of the library member.
class LibraryMember(models.Model):
    '''
       This class extends the models class.
    '''
    _name = 'library.member'
    _description = 'library.book: Stores library member details.'

    name = fields.Char(string='Member Name',required = True)
    email = fields.Char(string='Email ID',required = True)
    phone = fields.Char(string='Contact Number',required = True)
    membership_date = fields.Date(string='Membership Start Date')