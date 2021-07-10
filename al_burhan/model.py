#-*- coding: utf-8 -*- 
from odoo import models, fields, api
from openerp.exceptions import Warning, ValidationError
from datetime import datetime, timedelta , date
import webbrowser
import re
from odoo.exceptions import ValidationError

class BurhanCourse(models.Model): 
	_name = 'burhan.course'
	_description = 'Burhan Course'

	
	course_name = fields.Many2many("burhan.subjects",string="CourseName")


class BurhanSubjects(models.Model): 
	_name = 'burhan.subjects'
	_description = 'Burhan Subjects'

	name = fields.Char(string="Name")


class BurhanCampus(models.Model): 
	_name = 'burhan.campus'
	_description = 'Burhan Campus'

	name = fields.Char(string="Name")


class EcubeCity(models.Model): 
	_name = 'ecube.city'
	_description = 'Ecube City'

	_rec_name = 'city'
	city = fields.Char(string="City")


class EcubeResPatrtner(models.Model): 
	_name = 'ecube.res.partner'
	_description = 'Ecube Res Patrtner'

	name = fields.Char(string="Name")
	father_name = fields.Char(string="Father Name")
	date_of_birth = fields.Date(string="Date Of Birth")
	cnic = fields.Char(string='CNIC')
	mobile_number = fields.Char(string="Mobile Number")
	address = fields.Char(string="Address")
	city = fields.Many2one("ecube.city",string="City")
	nationality = fields.Char(string="Nationality")
	email = fields.Char(string="Email")
	gender = fields.Selection([
	('male','Male'),
	('female','Female')])

	def button(self):
		
		webbrowser.open('youtube.com',new=2)


	def host(self):

		webbrowser.open('192.168.18.54:8069', new=0)

	def google(self):
		webbrowser.open('google.com', new=1)


	@api.onchange('email')
	def validate_mail(self):
		if self.email:
			if len(str(self.email))>5:
				
				if not re.match('[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,3}$', str(self.email)):
					self.email=""
					return {'value':{},'warning':{'title':
					'warning','message':"invalid Email "+self.email+" type e:g abc@xyz.com"}}
				else:
					domain=self.email.split("@",1)[1]
					str2= ".."
					valid_email123= domain.find(str2)
					
					if valid_email123>0:
						self.email=""
						return {'value':{},'warning':{'title':
						'warning','message':"invalid Email "+self.email+" type e:g abc@xyz.com"}}
					else:
						pass
					
			else:
				self.email=""
				return {'value':{},'warning':{'title':
					'warning','message':"minimum leght is 6"}}





	# @api.onchange('gender')
	# def _onchange_gender(self):
	# 	if self.gender: 
	# 		self.name = str(self.gender)

	tree_id = fields.One2many('ecube.res.partner.tree', 'employee_name')

class EcubeResPatrtnerTree(models.Model): 
	_name = 'ecube.res.partner.tree'
	_description = 'Ecube Res Patrtner Tree'


	employee_name = fields.Many2one('ecube.res.partner',string="Employee Name")
	# employee_id = fields.Char(string="Employee ID")
	# department = fields.Char(string="Department")
	# experience = fields.Char(string="Experience")
	# skill_level = fields.Selection([('a', 'experienced'),('b', 'unexperienced'),('c', 'career_changer')],string="Skill Level")
	# start_date = fields.Date(string="Start Date")
	# end_date = fields.Date("End Date")



		


class CourseOffer(models.Model): 
	_name = 'course.offer'
	_description = 'Course Offer'
	# _rec_name = 'course_offer'

	course_offer = fields.Many2one("burhan.course",string="Course Offer")

	start_date = fields.Date(string="Start Date")
	end_date = fields.Date(string="End Date")
	tree_id = fields.One2many('course.offer.tree','campus')

class CourseOfferTree(models.Model): 
	_name = 'course.offer.tree'

	_description = 'Course Offer Tree'

	# _rec_name = 'city'
	campus = fields.Many2one('burhan.campus',string="Campus")
	start_date = fields.Date(string="Start Date")
	end_date = fields.Date(string="End Date")
	teacher = fields.Char(string="Teacher")










