from odoo import models, api


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    @api.onchange('fiscal_position_id')
    def somko_update_tax(self):
        for line in self.invoice_line_ids:
            line._onchange_product_id()
