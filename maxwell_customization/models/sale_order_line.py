# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from collections import defaultdict
from datetime import timedelta
from markupsafe import Markup

from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.fields import Command
from odoo.osv import expression
from odoo.tools import float_is_zero, float_compare, float_round, format_date, groupby


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'


    is_hidden = fields.Boolean(string="Is hidden")


    @api.depends('product_id', 'product_uom', 'product_uom_qty','is_hidden')
    def _compute_price_unit(self):
        super()._compute_price_unit()
        for line in self:
            if line.is_hidden:
                line.price_unit = 0

    def _prepare_invoice_line(self, **optional_values):
        res = super()._prepare_invoice_line(**optional_values)
        res['is_hidden'] = self.is_hidden
        return res