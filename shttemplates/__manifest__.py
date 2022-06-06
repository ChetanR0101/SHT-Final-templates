{
    'name' : "SHT Templates",
    'version' : "1.0",
    'author' : "Prisms",
    'summary': "",
    'description': "Multiple Template Designs",
    'depends' : ['base', 'account', 'sale'],
    'data' : [
      'security/ir.model.access.csv',

      'views/sht_invoice_view.xml',
      'views/sht_delivery_view.xml',
      'views/sht_product_view.xml',

      #report templates
      'report/report_action.xml',
      'report/invoice_s_template.xml',
      'report/invoice_us_template.xml',
      'report/credit_note_template.xml',
      'report/prepayment_s_template.xml',
      'report/prepayment_us_template.xml',
      'report/packing_list_template.xml',
      'report/proforma_invoice_template.xml',
      'report/delivery_order_template.xml',
      # 'report/delivery_order.xml',
            ],
    'css': [
      'shttemplates/static/src/css/main.css',
      ],
    # 'assets': {
    #     'web.assets_backend': [
    #       'shttemplates/static/src/css/main.css',
    #     ]
    # },
    'installable' : True,   
    'application' : True,
}
