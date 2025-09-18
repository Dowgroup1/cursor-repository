from odoo import models, fields


class HrEmployee(models.Model):
	_inherit = 'hr.employee'

	mobile_phone = fields.Char(string='Mobile Phone')
	birthday = fields.Date(string='Birthday')
	identification_id = fields.Char(string='Identification No.')