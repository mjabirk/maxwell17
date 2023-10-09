# -*- coding:utf-8 -*-
from odoo import fields, models


class HrContract(models.Model):
    _inherit = 'hr.contract'
    _description = 'Employee Contract'

    accommodation_allowance = fields.Monetary('Accommodation Allowance', default=0, tracking=True, help="Monthly Accommodation Allowance.")
    food_allowance = fields.Monetary('Food Allowance', default=0, tracking=True, help="Monthly Food Allowance.")
    transportation_allowance = fields.Monetary('Transportation Allowance', default=0, tracking=True, help="Monthly Transportation Allowance.")
    other_allowance = fields.Monetary('Other Allowance', default=0, tracking=True, help="Monthly Other Allowance.")
    rp_charge = fields.Monetary('RP Charge', default=0, tracking=True)
    air_ticket = fields.Monetary('Air Ticket', default=0, tracking=True)
    leave_pay_days = fields.Integer("Leave Pay Days")
    eos_days = fields.Integer("End Of Service Days")
    leave_period = fields.Integer("Leave Period")
