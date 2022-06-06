from odoo import models, fields


class SHT_Product(models.Model):
    _name = "sht.product"

    product_id = fields.Many2one(string="Product", comodel_name="product.product")
    name = fields.Char(string="Name", related='product_id.name')
    desc = fields.Text(string="Description")
    unit_price = fields.Float(string="Unit Price", digits=(12, 2))
    qty = fields.Integer(string="Quantity")

    invoice_id = fields.Many2one(string="Invoice Id", comodel_name="sht.invoice")
    delivery_id = fields.Many2one(string="Delivery Id", comodel_name="sht.delivery")