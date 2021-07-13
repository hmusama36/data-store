#-*- coding: utf-8 -*- 
from odoo import models, fields, api
from openerp.exceptions import Warning, ValidationError
from datetime import datetime, timedelta , date
class test_model(models.Model): 
	_name = 'test.model'
	_description = 'test_model'


	
	# _rec_name = 'car_name'
	test_name = fields.Many2one('res.partner',string="Test_Name")
	mobile= fields.Char(string="Mobile")
	email = fields.Char(string="Email")
	job_position = fields.Char(string='Job_Position')
	age =fields.Char(string="Age")
	address = fields.Char(string="Address")

	details_id = fields.One2many('details.test','return_link')


	@api.onchange('test_name')
	def getdiff(self):
		print "===========onchange=========="
		self.mobile=self.test_name.mobile
		self.email=self.test_name.email
		# self.address=self.test_name.address
	

	@api.multi
	def write(self, vals):
		super(test_model, self).write(vals)
		print "============write============="


	@api.model
	def create(self, vals):
		Res = super(test_model,self).create(vals)
		print "================create============="
		return Res


	@api.multi
	def unlink(self):
		given = super(test_model,self).unlink()
		print "==============delete==============="
		return given



	@api.multi
	def draft(self):
		for rec in self:
			rec.state = 'draft'
	
	
	@api.multi
	def validate(self):
		for rec in self:
			rec.state = 'validate'


class DetailsName(models.Model):
	_name = "details.test"

	name=fields.Char(string="Name")
	owner=fields.Char(string="Owner")
	made=fields.Char(string="Made")
	return_link=fields.Many2one('test_name')