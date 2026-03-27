from odoo import models, _
from odoo.exceptions import ValidationError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        for order in self:
            if order.amount_total < 500_000:
                raise ValidationError(_("Minimal order value adalah 500.000"))
        return super(SaleOrder, self).action_confirm()