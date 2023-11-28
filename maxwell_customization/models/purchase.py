# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from collections import defaultdict

from odoo import api, fields, models, _


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    project = fields.Char("Project")
    prepared_id = fields.Many2one('hr.employee', string='Prepared By')
    verified_id = fields.Many2one('hr.employee', string='Verified By')
    approved_id = fields.Many2one('hr.employee', string='Approved By')