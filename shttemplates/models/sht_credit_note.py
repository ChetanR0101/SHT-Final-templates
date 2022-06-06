from odoo import models, fields

class ShtCredit(models.Model):
    _name = 'sht.credit.note'
    
    name = fields.Char(string='Name')
