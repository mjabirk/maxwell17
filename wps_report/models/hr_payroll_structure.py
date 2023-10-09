#-*- coding:utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class HrPayrollStructure(models.Model):
    _inherit = 'hr.payroll.structure'


    @api.model
    def _get_default_rule_ids(self):
        return [
            (0, 0, {
                'name': _('Basic Salary'),
                'sequence': 1,
                'code': 'BASIC',
                'category_id': self.env.ref('hr_payroll.BASIC').id,
                'condition_select': 'none',
                'amount_select': 'code',
                'amount_python_compute': """Paid_Days = 0
if worked_days.WORK100:
    Paid_Days += worked_days.WORK100.number_of_days
if worked_days.LEAVE105:
    Paid_Days += worked_days.LEAVE105.number_of_days
if worked_days.LEAVE110:
    Paid_Days += worked_days.LEAVE110.number_of_days
if worked_days.Termination:
    Paid_Days += worked_days.Termination.number_of_days
if worked_days.Resignation:
    Paid_Days += worked_days.Resignation.number_of_days
if worked_days.Business:
    Paid_Days += worked_days.Business.number_of_days
if worked_days.Sick_Leave:
    Paid_Days += worked_days.Sick_Leave.number_of_days
if worked_days.Leave_Reimbursement:
    Paid_Days += worked_days.Leave_Reimbursement.number_of_days
	
month = payslip.date_from.month
year = payslip.date_from.year
if(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12): tot_days = 31
elif((month == 2) and ((year%400==0) or (year%4==0 and year%100!=0))): tot_days = 29
elif(month == 2): tot_days = 28
else: tot_days = 30
	
result = round((tot_days ) and contract.wage*Paid_Days/(tot_days ) or 0)""",
            }),
            (0, 0, {
                'name': _('Accommodation Allowances'),
                'sequence': 20,
                'code': 'ACCO',
                'category_id': self.env.ref('hr_payroll.ALW').id,
                'condition_select': 'python',
                'condition_python': 'result = contract.accommodation_allowance > 0',
                'amount_select': 'code',
                'amount_python_compute': """Paid_Days = 0
if worked_days.WORK100:
    Paid_Days += worked_days.WORK100.number_of_days
if worked_days.LEAVE105:
    Paid_Days += worked_days.LEAVE105.number_of_days
if worked_days.LEAVE110:
    Paid_Days += worked_days.LEAVE110.number_of_days
if worked_days.Termination:
    Paid_Days += worked_days.Termination.number_of_days
if worked_days.Resignation:
    Paid_Days += worked_days.Resignation.number_of_days
if worked_days.Business:
    Paid_Days += worked_days.Business.number_of_days
if worked_days.Sick_Leave:
    Paid_Days += worked_days.Sick_Leave.number_of_days
if worked_days.Leave_Reimbursement:
    Paid_Days += worked_days.Leave_Reimbursement.number_of_days
	
month = payslip.date_from.month
year = payslip.date_from.year
if(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12): tot_days = 31
elif((month == 2) and ((year%400==0) or (year%4==0 and year%100!=0))): tot_days = 29
elif(month == 2): tot_days = 28
else: tot_days = 30
	
result =round((tot_days ) and contract.accommodation_allowance*Paid_Days/(tot_days ) or 0)""",
            }),
            (0, 0, {
                'name': _('Food Allowances'),
                'sequence': 25,
                'code': 'FOOD',
                'category_id': self.env.ref('hr_payroll.ALW').id,
                'condition_select': 'python',
                'condition_python': 'result = contract.food_allowance > 0',
                'amount_select': 'code',
                'amount_python_compute': """Paid_Days = 0
if worked_days.WORK100:
    Paid_Days += worked_days.WORK100.number_of_days
if worked_days.LEAVE105:
    Paid_Days += worked_days.LEAVE105.number_of_days
if worked_days.LEAVE110:
    Paid_Days += worked_days.LEAVE110.number_of_days
if worked_days.Termination:
    Paid_Days += worked_days.Termination.number_of_days
if worked_days.Resignation:
    Paid_Days += worked_days.Resignation.number_of_days
if worked_days.Business:
    Paid_Days += worked_days.Business.number_of_days
if worked_days.Sick_Leave:
    Paid_Days += worked_days.Sick_Leave.number_of_days
if worked_days.Leave_Reimbursement:
    Paid_Days += worked_days.Leave_Reimbursement.number_of_days
	
month = payslip.date_from.month
year = payslip.date_from.year
if(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12): tot_days = 31
elif((month == 2) and ((year%400==0) or (year%4==0 and year%100!=0))): tot_days = 29
elif(month == 2): tot_days = 28
else: tot_days = 30	
result = round( (tot_days ) and contract.food_allowance*Paid_Days/(tot_days ) or 0)""",
            }),
            (0, 0, {
                'name': _('Transportation Allowances'),
                'sequence': 30,
                'code': 'TRANS',
                'category_id': self.env.ref('hr_payroll.ALW').id,
                'condition_select': 'python',
                'condition_python': 'result = contract.transportation_allowance > 0',
                'amount_select': 'code',
                'amount_python_compute': """Paid_Days = 0
if worked_days.WORK100:
    Paid_Days += worked_days.WORK100.number_of_days
if worked_days.LEAVE105:
    Paid_Days += worked_days.LEAVE105.number_of_days
if worked_days.LEAVE110:
    Paid_Days += worked_days.LEAVE110.number_of_days
if worked_days.Termination:
    Paid_Days += worked_days.Termination.number_of_days
if worked_days.Resignation:
    Paid_Days += worked_days.Resignation.number_of_days
if worked_days.Business:
    Paid_Days += worked_days.Business.number_of_days
if worked_days.Sick_Leave:
    Paid_Days += worked_days.Sick_Leave.number_of_days
if worked_days.Leave_Reimbursement:
    Paid_Days += worked_days.Leave_Reimbursement.number_of_days
	
month = payslip.date_from.month
year = payslip.date_from.year
if(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12): tot_days = 31
elif((month == 2) and ((year%400==0) or (year%4==0 and year%100!=0))): tot_days = 29
elif(month == 2): tot_days = 28
else: tot_days = 30	
result = round((tot_days ) and contract.transportation_allowance*Paid_Days/(tot_days ) or 0)""",
            }),
            (0, 0, {
                'name': _('Other Allowances'),
                'sequence': 35,
                'code': 'OTHER',
                'category_id': self.env.ref('hr_payroll.ALW').id,
                'condition_select': 'python',
                'condition_python': 'result = contract.other_allowance > 0',
                'amount_select': 'code',
                'amount_python_compute': """Paid_Days = 0
if worked_days.WORK100:
    Paid_Days += worked_days.WORK100.number_of_days
if worked_days.LEAVE105:
    Paid_Days += worked_days.LEAVE105.number_of_days
if worked_days.LEAVE110:
    Paid_Days += worked_days.LEAVE110.number_of_days
if worked_days.Termination:
    Paid_Days += worked_days.Termination.number_of_days
if worked_days.Resignation:
    Paid_Days += worked_days.Resignation.number_of_days
if worked_days.Business:
    Paid_Days += worked_days.Business.number_of_days
if worked_days.Sick_Leave:
    Paid_Days += worked_days.Sick_Leave.number_of_days
if worked_days.Leave_Reimbursement:
    Paid_Days += worked_days.Leave_Reimbursement.number_of_days
	
month = payslip.date_from.month
year = payslip.date_from.year
if(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12): tot_days = 31
elif((month == 2) and ((year%400==0) or (year%4==0 and year%100!=0))): tot_days = 29
elif(month == 2): tot_days = 28
else: tot_days = 30	
result = round((tot_days ) and contract.other_allowance*Paid_Days/(tot_days ) or 0)""",
            }),
            (0, 0, {
                'name': _('Overtime Hours'),
                'sequence': 40,
                'code': 'OT',
                'category_id': self.env.ref('hr_payroll.ALW').id,
                'condition_select': 'python',
                'condition_python': 'result =worked_days.OT and worked_days.OT.number_of_hours',
                'amount_select': 'code',
                'amount_python_compute': """DAYS_PER_MONTH = 365.0 / 12
WORKING_TIME = 8
rate = contract.wage / DAYS_PER_MONTH / WORKING_TIME
result = round((worked_days.OT and worked_days.OT.number_of_hours*rate or 0)
result_name = 'Over Time for ' + str(worked_days.OT.number_of_hours) + 'Hours'""",
            }),
            (0, 0, {
                'name': _('Overtime Amount'),
                'sequence': 45,
                'code': 'OTA',
                'category_id': self.env.ref('hr_payroll.ALW').id,
                'condition_select': 'python',
                'condition_python': 'result =inputs.OT and inputs.OT.amount',
                'amount_select': 'code',
                'amount_python_compute': """result = (inputs.OT and inputs.OT.amount or 0)
result_name = inputs.OT and inputs.OT.name or 'Over Time Amount'""",
            }),
            (0, 0, {
                'name': _('Air Ticket'),
                'sequence': 50,
                'code': 'AIRTKT',
                'category_id': self.env.ref('hr_payroll.ALW').id,
                'condition_select': 'python',
                'condition_python': 'result = (worked_days.Leave_Reimbursement or worked_days.Termination or worked_days.Annual)',
                'amount_select': 'code',
                'amount_python_compute': """result = 0
if inputs.AT and inputs.AT.amount:
    result  = inputs.AT.amount
else:
    if  (worked_days.Leave_Reimbursement or worked_days.Termination or worked_days.Annual) :
        if contract.structure_type_id.name == 'Employee':
            result +=round( contract.air_ticket)
        else:
            result += round(contract.air_ticket*.75)""",
            }),
            (0, 0, {
                'name': _('Leave Pay'),
                'sequence': 55,
                'code': 'LP',
                'category_id': self.env.ref('hr_payroll.ALW').id,
                'condition_select': 'python',
                'condition_python': 'result = worked_days.Termination or worked_days.Resignation or worked_days.Annual',
                'amount_select': 'code',
                'amount_python_compute': """date_from = contract.date_start

previous_annual_leaves=employee.leave_ids.search([('employee_id','=',employee.id),('state','=','validate'),('request_date_from','<',payslip.date_from),('request_date_from','>=',date_from),('holiday_status_id.name','in',['Annual'])],order='request_date_from desc')
if previous_annual_leaves:
    date_from  = previous_annual_leaves[0].request_date_to

date_to = payslip.date_from
leaves=employee.leave_ids.search([('employee_id','=',employee.id),('state','=','validate'),('request_date_from','<=',payslip.date_to),('request_date_from','>=',payslip.date_from),('holiday_status_id.name','in',['Termination','Resignation'])])
if leaves:
    date_to  = leaves[0].request_date_from
unpaid_leaves=employee.leave_ids.search([('employee_id','=',employee.id),('state','=','validate'),('request_date_from','>=',date_from),('request_date_from','<=',payslip.date_from),('holiday_status_id.name','in',['Unpaid'])])
unpaid_days=0
for unpaid_leave in unpaid_leaves:
    unpaid_days += unpaid_leave.number_of_days
delay = (date_to  -date_from ).days - unpaid_days 
result = round(((contract.wage + contract.accommodation_allowance) * contract.leave_pay_days * 12 * delay  / (365 * 365)) or 0)""",
            }),
            (0, 0, {
                'name': _('End of Service'),
                'sequence': 65,
                'code': 'EOS',
                'category_id': self.env.ref('hr_payroll.ALW').id,
                'condition_select': 'python',
                'condition_python': 'result = worked_days.Termination  or  worked_days.Resignation ',
                'amount_select': 'code',
                'amount_python_compute': """#date_from = contract.date_start
date_from = employee.joining_date
date_to = payslip.date_from
leaves=employee.leave_ids.search([('employee_id','=',employee.id),('state','=','validate'),('request_date_from','<=',payslip.date_to),('request_date_from','>=',payslip.date_from),('holiday_status_id.name','in',['Termination','Resignation'])])
if leaves:
    date_to  = leaves[0].request_date_from
delay = (date_to  -date_from ).days

unpaid_leaves=employee.leave_ids.search([('employee_id','=',employee.id),('state','=','validate'),('request_date_from','>=',date_from),('request_date_from','<=',payslip.date_from),('holiday_status_id.name','in',['Unpaid'])])
unpaid_days=0
for unpaid_leave in unpaid_leaves:
    unpaid_days += unpaid_leave.number_of_days
if unpaid_days  <= 31:
    unpaid_days   = 0
else:
    unpaid_days -= 31
result = round((contract.wage  * contract.eos_days * 12 * (delay-unpaid_days)  / (365 * 365)) or 0)""",
            }),
            (0, 0, {
                'name': _('Gross'),
                'sequence': 100,
                'code': 'GROSS',
                'category_id': self.env.ref('hr_payroll.GROSS').id,
                'condition_select': 'none',
                'amount_select': 'code',
                'amount_python_compute': 'result = categories.BASIC + categories.ALW',
            }),
            (0, 0, {
                'name': _('Leave Pay Accrual'),
                'sequence': 150,
                'code': 'LPAC',
                'category_id': self.env.ref('hr_payroll.COMP').id,
                'condition_select': 'none',
                'amount_select': 'code',
                'appears_on_payslip':False,
                'amount_python_compute': """Paid_Days = 0
if worked_days.WORK100:
    Paid_Days += worked_days.WORK100.number_of_days
if worked_days.LEAVE105:
    Paid_Days += worked_days.LEAVE105.number_of_days
if worked_days.LEAVE110:
    Paid_Days += worked_days.LEAVE110.number_of_days
if worked_days.Termination:
    Paid_Days += worked_days.Termination.number_of_days
if worked_days.Resignation:
    Paid_Days += worked_days.Resignation.number_of_days
if worked_days.Business:
    Paid_Days += worked_days.Business.number_of_days
if worked_days.Sick_Leave:
    Paid_Days += worked_days.Sick_Leave.number_of_days
if worked_days.Leave_Reimbursement:
    Paid_Days += worked_days.Leave_Reimbursement.number_of_days

month = payslip.date_from.month
year = payslip.date_from.year
if(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12): tot_days = 31
elif((month == 2) and ((year%400==0) or (year%4==0 and year%100!=0))): tot_days = 29
elif(month == 2): tot_days = 28
else: tot_days = 30	
result = tot_days and round((contract.wage+ contract.accommodation_allowance)*contract.leave_pay_days*Paid_Days /(365*tot_days)) or 0""",
            }),
            (0, 0, {
                'name': _('End of Service Accrual'),
                'sequence': 155,
                'code': 'EOSAC',
                'category_id': self.env.ref('hr_payroll.COMP').id,
                'condition_select': 'none',
                'appears_on_payslip':False,
                'amount_select': 'code',
                'amount_python_compute': """Paid_Days = 0
if worked_days.LEAVE90:
    Paid_Days += worked_days.LEAVE90.number_of_days
if worked_days.WORK100:
    Paid_Days += worked_days.WORK100.number_of_days
if worked_days.LEAVE105:
    Paid_Days += worked_days.LEAVE105.number_of_days
if worked_days.LEAVE110:
    Paid_Days += worked_days.LEAVE110.number_of_days
if worked_days.Termination:
    Paid_Days += worked_days.Termination.number_of_days
if worked_days.Resignation:
    Paid_Days += worked_days.Resignation.number_of_days
if worked_days.Business:
    Paid_Days += worked_days.Business.number_of_days
if worked_days.Sick_Leave:
    Paid_Days += worked_days.Sick_Leave.number_of_days
if worked_days.Leave_Reimbursement:
    Paid_Days += worked_days.Leave_Reimbursement.number_of_days
if worked_days.Annual:
    Paid_Days += worked_days.Annual.number_of_days

month = payslip.date_from.month
year = payslip.date_from.year
if(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12): tot_days = 31
elif((month == 2) and ((year%400==0) or (year%4==0 and year%100!=0))): tot_days = 29
elif(month == 2): tot_days = 28
else: tot_days = 30
result = tot_days  and round(contract.wage * contract.eos_days * Paid_Days / (365 * tot_days )) or 0""",
            }),
            (0, 0, {
                'name': _('Deduction'),
                'sequence': 198,
                'code': 'DEDUCTION',
                'category_id': self.env.ref('hr_payroll.DED').id,
                'condition_select': 'python',
                'condition_python': 'result = inputs.DEDUCTION',
                'amount_select': 'code',
                'amount_python_compute': """result = -inputs.DEDUCTION.amount
result_name = inputs.DEDUCTION.name""",
            }),
            (0, 0, {
                'name': _('Net Salary'),
                'sequence': 200,
                'code': 'NET',
                'category_id': self.env.ref('hr_payroll.NET').id,
                'condition_select': 'none',
                'amount_select': 'code',
                'amount_python_compute': 'result = categories.BASIC + categories.ALW + categories.DED',
            })
        ]

    rule_ids = fields.One2many(
        'hr.salary.rule', 'struct_id',
        string='Salary Rules', default=_get_default_rule_ids)