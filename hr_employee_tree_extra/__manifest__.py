{
	'name': 'HR Employee Tree Extra',
	'Version': '18.0.1.0.0',
	'summary': 'Adds extra fields to the Employee tree view.',
	'description': 'Inherits the standard hr.employee tree view and adds mobile_phone, birthday, identification_id. Includes minimal model and access rules.',
	'author': 'Your Company',
	'category': 'Human Resources',
	'website': 'https://example.com',
	'license': 'LGPL-3',
	'depends': ['hr'],
	'data': [
		'security/ir.model.access.csv',
		'security/hr_employee_rules.xml',
		'views/hr_employee_views.xml',
	],
	'installable': True,
	'application': False,
	'auto_install': False,
}