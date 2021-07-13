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


	name = fields.Char(string="Name")
	course_name = fields.Many2many("burhan.subjects",string="Subject Name")


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
		
		webbrowser.open('alburhan.org',new=2)


	# def host(self):

	# 	webbrowser.open('192.168.18.54:8069', new=0)

	# def google(self):
	# 	webbrowser.open('google.com', new=1)


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





	@api.model
	def create(self,val):
		record = super(EcubeResPatrtner, self).create(val)
		record.create_application_form()
		return record

	def write(self,val):

		record = super(EcubeResPatrtner, self).write(val)
		self.create_application_form()
		return record

	def create_application_form(self):
		application_form = self.env['application.form']
		new_record_create_id = application_form.create({
			'applicant_name' : self.name,
			'f_name' : self.father_name,
			'cnic' : self.cnic,
			'address' : self.address,
			'mobile_number' : self.mobile_number,
			'email' : self.email,
			})

class CourseOffer(models.Model): 
	_name = 'course.offer'
	_description = 'Course Offer'
	# _rec_name = 'name'

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


class ApplicationForm(models.Model): 
	_name = 'application.form'
	_description = 'Form'
	# _rec_name = 'name'

	applicant_name = fields.Char(string="Applicant Name")
	f_name = fields.Char(string="Father Name")
	cnic = fields.Char(string='Applicant CNIC')
	address = fields.Char(string="Applicant Address")
	mobile_number = fields.Char(string="Mobile Number")
	email = fields.Char(string="Applicant Email")
	gender = fields.Selection([
	('male','Male'),
	('female','Female')], string="Applicant Gender")

	course = fields.Many2one("burhan.course",string="Apply Course")
	campus = fields.Many2one("burhan.campus",string="Apply Campus")
	date = fields.Date(string="Apply Date")
	stage = fields.Selection([
	('draft','Draft'),
	('interview_call','Interview Call'),
	('first_interview','First Interview'),
	('second_interview','Second Interview'),
	('enrollment','Enrollment')], default='draft')



	def draft(self):
		self.stage = 'draft'

	def call(self):
		self.stage = 'interview_call'
	def first(self):
		self.stage = 'first_interview'
	def second(self):
		self.stage = 'second_interview'
	def enroll(self):
		self.stage = 'enrollment'


	
		create = self.env['ecube.res.partner'].create({
		'name': self.applicant_name,
		'father_name': self.f_name,
		'cnic': self.cnic,
		'address': self.address,
		'mobile_number': self.mobile_number,
		'email': self.email,})









