from odoo import models, fields

class ShtDelivery(models.Model):
    _name = 'sht.delivery'
    
    name = fields.Char(string='Name')
    to = fields.Text(string="To")
    add = fields.Text(string="Address")
    date = fields.Date(string="Date")
    vessel = fields.Char("Vessel :")
    co = fields.Char("C/O") 
    po_no = fields.Integer("PO No.")
    order_no = fields.Integer("Delivery Order No")
    pic = fields.Integer("PIC")
    tel = fields.Char(string="Tel")
    project = fields.Char(string="Project")
    attn = fields.Char("ATTN")

    product_ids = fields.One2many(comodel_name="sht.product", string="Item Name",inverse_name="delivery_id")