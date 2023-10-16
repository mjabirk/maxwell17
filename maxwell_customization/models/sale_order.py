# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.tools import float_compare
###
###     Move this to customer invoice and add it in view and


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    po_received_date = fields.Date(string='PO Received on')
    po_received_date = fields.Date(string='Work Completed on')