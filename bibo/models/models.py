# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, date, time
from dateutil.relativedelta import relativedelta
from odoo import exceptions, _
from openerp.exceptions import UserError, RedirectWarning, ValidationError
import sys


class lead_ini(models.Model):
	_inherit='crm.lead'

	piezas=fields.Integer(string='Numero de Piezas', index=True)
	estados =  fields.Many2one('res.country.state',domain="[('country_id.code','=','MX')]", string="Estado")
	estado=fields.Integer(string='Estado', index=True)
	type_cliente=fields.Char(string='¿Cliente/provedor?', index=True)

	@api.model
	def create(self,values):
		if values:
			res = super(lead_ini, self).create(values)
			if res['type_cliente'] == 'Proveedor':
				if res['piezas'] >= 200:
					if res['estado'] == 3 or res['estado'] == 4 or res['estado'] == 26 or res['estado'] == 27 or res['estado'] == 7 or res['estado'] == 8 or res['estado'] == 11 or res['estado'] == 29:
						res['contact_name']
						res['description']
						res['email_from']
						res['name']
						res['partner_name']
						res['phone']
						res['team_id']
						res['piezas']
						res['estado']
						res['type_cliente']
						res['function']
						r= 'asesor@bibo.com.mx'
						r2 = self.env['res.users'].search([('login', '=', r)], limit=1)
						if r2:
							res['user_id'] = r2.id
							res['team_id'] = r2.sale_team_id
							return res
					elif res['estado'] == 2 or res['estado'] == 12 or res['estado'] == 23 or res['estado'] == 25 or res['estado'] == 33 or res['estado'] == 15 or res['estado'] == 9 or res['estado'] == 19  or res['estado'] == 16 or res['estado'] == 13 or res['estado'] == 22:
						res['contact_name']
						res['description']
						res['email_from']
						res['name']
						res['partner_name']
						res['phone']
						res['team_id']
						res['user_id']
						res['piezas']
						res['estado']
						res['type_cliente']
						res['function']
						r= 'asesor.occidente@bibo.com.mx'
						r2 = self.env['res.users'].search([('login', '=', r)], limit=1)
						if r2:
							res['user_id'] = r2.id
							res['team_id'] = r2.sale_team_id
							return res
					elif res['estado'] != 3 or res['estado'] != 4 or res['estado'] != 26 or res['estado'] != 27 or res['estado'] != 7 or res['estado'] != 8 or res['estado'] != 11 or res['estado'] != 29 or res['estado'] != 2 or res['estado'] != 12 or res['estado'] != 23 or res['estado'] != 25 or res['estado'] != 33 or res['estado'] != 15 or res['estado'] != 9 or res['estado'] != 19  or res['estado'] != 16 or res['estado'] != 13 or res['estado'] != 22:
						res['contact_name']
						res['description']
						res['email_from']
						res['name']
						res['partner_name']
						res['phone']
						res['team_id']
						res['user_id']
						res['piezas']
						res['estado']
						res['type_cliente']
						res['function']
						res['user_id'] = ''
						res['team_id'] = ''
						return res
				else:
					if res['piezas']>=1 and res['piezas']<=199:
						if res['estado'] == 3 or res['estado'] == 4 or res['estado'] ==26 or res['estado'] == 27:
							res['contact_name']
							res['description']
							res['email_from']
							res['name']
							res['partner_name']
							res['phone']
							res['team_id']
							res['user_id']
							res['piezas']
							res['estado']
							res['type_cliente']
							res['function']
							r= 'mayoreo.pacifico@bibo.com.mx'
							r2 = self.env['res.users'].search([('login', '=', r)], limit=1)
							if r2:
								res['user_id'] = r2.id
								res['team_id'] = r2.sale_team_id
								return res
						elif res['estado'] == 7 or res['estado'] == 8 or res['estado'] == 29 or res['estado'] == 11 or res['estado'] == 9 or res['estado'] == 19:
							res['contact_name']
							res['description']
							res['email_from']
							res['name']
							res['partner_name']
							res['phone']
							res['team_id']
							res['user_id']
							res['piezas']
							res['estado']
							res['type_cliente']
							res['function']
							r= 'mayoreo.norte@bibo.com.mx'
							r2 = self.env['res.users'].search([('login', '=', r)], limit=1)
							if r2:
								res['user_id'] = r2.id
								res['team_id'] = r2.sale_team_id
								return res
						elif res['estado'] == 2 or res['estado'] == 12 or res['estado'] == 23 or res['estado'] == 25 or res['estado'] == 33:
							res['contact_name']
							res['description']
							res['email_from']
							res['name']
							res['partner_name']
							res['phone']
							res['team_id']
							res['user_id']
							res['piezas']
							res['estado']
							res['type_cliente']
							res['function']
							r= 'mayoreo.bajio@bibo.com.mx'
							r2 = self.env['res.users'].search([('login', '=', r)], limit=1)
							if r2:
								res['user_id'] = r2.id
								res['team_id'] = r2.sale_team_id
								return res
						elif res['estado'] == 15 or res['estado'] == 16:
							res['contact_name']
							res['description']
							res['email_from']
							res['name']
							res['partner_name']
							res['phone']
							res['team_id']
							res['user_id']
							res['piezas']
							res['estado']
							res['type_cliente']
							res['function']
							r= 'mayoreo.occidente@bibo.com.mx'
							r2 = self.env['res.users'].search([('login', '=', r)], limit=1)
							if r2:
								res['user_id'] = r2.id
								res['team_id'] = r2.sale_team_id
								return res
						elif res['estado'] == 10 or res['estado'] == 18 or res['estado'] == 14 or res['estado'] == 17 or res['estado'] == 30:
							res['contact_name']
							res['description']
							res['email_from']
							res['name']
							res['partner_name']
							res['phone']
							res['team_id']
							res['user_id']
							res['piezas']
							res['estado']
							res['type_cliente']
							res['function']
							r= 'mayoreo.centro@bibo.com.mx'
							r2 = self.env['res.users'].search([('login', '=', r)], limit=1)
							if r2:
								res['user_id'] = r2.id
								res['team_id'] = r2.sale_team_id
								return res
						elif res['estado'] == 32 or res['estado'] == 5 or res['estado'] == 24 or res['estado'] == 6 or res['estado'] == 21 or res['estado'] == 31 or res['estado'] == 28 or res['estado'] == 22 or res['estado'] == 13: 
							res['contact_name']
							res['description']
							res['email_from']
							res['name']
							res['partner_name']
							res['phone']
							res['team_id']
							res['user_id']
							res['piezas']
							res['estado']
							res['type_cliente']
							res['function']
							r= 'mayoreo.sureste@bibo.com.mx'
							r2 = self.env['res.users'].search([('login', '=', r)], limit=1)
							if r2:
								res['user_id'] = r2.id
								res['team_id'] = r2.sale_team_id
								return res
						elif res['estado'] != 3 or res['estado'] != 4 or res['estado'] !=26 or res['estado'] != 27 or res['estado'] != 7 or res['estado'] != 8 or res['estado'] != 29 or res['estado'] != 11 or res['estado'] != 9 or res['estado'] != 19 or res['estado'] != 2 or res['estado'] != 12 or res['estado'] != 23 or res['estado'] != 25 or res['estado'] != 33 or  res['estado'] != 15 or res['estado'] != 16 or res['estado'] != 10 or res['estado'] != 18 or res['estado'] != 14 or res['estado'] != 17 or res['estado'] != 30 or res['estado'] != 32 or res['estado'] != 5 or res['estado'] != 24 or res['estado'] != 6 or res['estado'] != 21 or res['estado'] != 31 or res['estado'] != 28 or res['estado'] != 22 or res['estado'] != 13:
							res['contact_name']
							res['description']
							res['email_from']
							res['name']
							res['partner_name']
							res['phone']
							res['team_id']
							res['user_id']
							res['piezas']
							res['estado']
							res['type_cliente']
							res['function']
							res['user_id'] = ''
							res['team_id'] = ''
							return res
			else:
				if res['piezas'] >= 1 and res['piezas'] <= 500:
					res['contact_name']
					res['description']
					res['email_from']
					res['name']
					res['partner_name']
					res['phone']
					res['team_id']
					res['piezas']
					res['estado']
					res['type_cliente']
					res['function']
					r= 'l.galaviz@isauniformes.com'
					r2 = self.env['res.users'].search([('login', '=', r)], limit=1)
					if r2:
						res['user_id'] = r2.id
						res['team_id'] = r2.sale_team_id
						return res
				else:
					res['contact_name']
					res['description']
					res['email_from']
					res['name']
					res['partner_name']
					res['phone']
					res['team_id']
					res['user_id']
					res['piezas']
					res['estado']
					res['type_cliente']
					res['function']
					r= 'guillermowilliams@bibo.com.mx'
					r2 = self.env['res.users'].search([('login', '=', r)], limit=1)
					if r2:
						res['user_id'] = r2.id
						res['team_id'] = r2.sale_team_id
						return res