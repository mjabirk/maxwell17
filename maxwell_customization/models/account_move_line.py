import ast
from collections import defaultdict
from contextlib import contextmanager
from datetime import date, timedelta
from functools import lru_cache
from markupsafe import escape

from odoo import api, fields, models, Command, _
from odoo.exceptions import ValidationError, UserError
from odoo.osv import expression
from odoo.tools import frozendict, formatLang, format_date, float_compare
from odoo.tools.sql import create_index
from odoo.addons.web.controllers.utils import clean_action

from odoo.addons.account.models.account_move import MAX_HASH_VERSION


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'


    is_hidden = fields.Boolean(string="Is hidden")

    #
    # @api.depends('product_id', 'product_uom', 'product_uom_qty','is_hidden')
    # def _compute_price_unit(self):
    #     super()._compute_price_unit()
    #     for line in self:
    #         if line.is_hidden:
    #             line.price_unit = 0
    #
    #
    # # === Price fields === #
    # price_unit = fields.Float(
    #     string='Unit Price',
    #     compute="_compute_price_unit", store=True, readonly=False, precompute=True,
    #     digits='Product Price',
    # )
    # price_subtotal = fields.Monetary(
    #     string='Subtotal',
    #     compute='_compute_totals', store=True,
    #     currency_field='currency_id',
    # )
    # price_total = fields.Monetary(
    #     string='Total',
    #     compute='_compute_totals', store=True,
    #     currency_field='currency_id',
    # )
    # @api.depends('quantity', 'discount', 'price_unit', 'tax_ids', 'currency_id')
    # def _compute_totals(self):
    #     for line in self:
    #         if line.display_type != 'product':
    #             line.price_total = line.price_subtotal = False
    #         # Compute 'price_subtotal'.
    #         line_discount_price_unit = line.price_unit * (1 - (line.discount / 100.0))
    #         subtotal = line.quantity * line_discount_price_unit
    #
    #         # Compute 'price_total'.
    #         if line.tax_ids:
    #             taxes_res = line.tax_ids.compute_all(
    #                 line_discount_price_unit,
    #                 quantity=line.quantity,
    #                 currency=line.currency_id,
    #                 product=line.product_id,
    #                 partner=line.partner_id,
    #                 is_refund=line.is_refund,
    #             )
    #             line.price_subtotal = taxes_res['total_excluded']
    #             line.price_total = taxes_res['total_included']
    #         else:
    #             line.price_total = line.price_subtotal = subtotal
    #
    # @api.depends('product_id', 'product_uom_id')
    # def _compute_price_unit(self):
    #     for line in self:
    #         if not line.product_id or line.display_type in ('line_section', 'line_note'):
    #             continue
    #         if line.move_id.is_sale_document(include_receipts=True):
    #             document_type = 'sale'
    #         elif line.move_id.is_purchase_document(include_receipts=True):
    #             document_type = 'purchase'
    #         else:
    #             document_type = 'other'
    #         line.price_unit = line.product_id._get_tax_included_unit_price(
    #             line.move_id.company_id,
    #             line.move_id.currency_id,
    #             line.move_id.date,
    #             document_type,
    #             fiscal_position=line.move_id.fiscal_position_id,
    #             product_uom=line.product_uom_id,
    #         )
