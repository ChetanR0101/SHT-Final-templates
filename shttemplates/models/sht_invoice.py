from odoo import models, fields

class ShtInvoice(models.Model):
    _name = 'sht.invoice'
    # _inherit = 'account.move'
    name = fields.Char(string="Name")
    to = fields.Text(string='To')
    date =fields.Date(string="Date") # date
    invoice_no=fields.Integer("Invoice No") # Invoice No
    order_no=fields.Char("Order No") # YOUR ORDER NO:
    ref=fields.Char("REF ") #  OUR REF:
    terms= fields.Char("Terms") # Terms
    vendor_code= fields.Char("Vendor Code") # vendor code
    job_id= fields.Char("Job ID") # job id
    attn=fields.Char("ATTN") # ATTN

    product_ids = fields.One2many(comodel_name="sht.product", inverse_name="invoice_id", string="Products")