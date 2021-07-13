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


	_rec_name = 'name'

	name = fields.Char(string="Name")
	course_name = fields.Many2many("burhan.subjects",string="Subject Name")


class BurhanSubjects(models.Model): 
	_name = 'burhan.subjects'
	_description = 'Burhan Subjects'
	_rec_name = 'name'

	name = fields.Char(string="Name")


class BurhanCampus(models.Model): 
	_name = 'burhan.campus'
	_description = 'Burhan Campus'

	_rec_name = 'name'

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
	cnic = fields.Char(string='CNIC')
	mobile_number = fields.Char(string="Mobile Number")
	address = fields.Char(string="Address")
	city = fields.Many2one("ecube.city",string="City")
	nationality = fields.Char(string="Nationality")
	email = fields.Char(string="Email")
	course = fields.Many2one("burhan.course",string="Apply Course")
	campus = fields.Many2one("burhan.campus",string="Apply Campus")
	date = fields.Date(string="Apply Date")
	gender = fields.Selection([
	('male','Male'),
	('female','Female')])

	def button(self):
		
		webbrowser.open('alburhan.org',new=2)
	


class CourseOffer(models.Model): 
	_name = 'course.offer'
	_description = 'Course Offer'

	course_offer = fields.Char(string="Course Offer")

	start_date = fields.Date(string="Start Date")
	end_date = fields.Date(string="End Date")
	tree_id = fields.One2many('course.offer.tree','campus')

class CourseOfferTree(models.Model): 
	_name = 'course.offer.tree'

	_description = 'Course Offer Tree'

	campus = fields.Many2one('burhan.campus',string="Campus")
	start_date = fields.Date(string="Start Date")
	end_date = fields.Date(string="End Date")
	teacher = fields.Char(string="Teacher")


class ApplicationForm(models.Model): 
	_name = 'application.form'
	_description = 'Form'

	# _rec_name = 'campus_id'


	applicant_name = fields.Char(string="Applicant Name", required=True)
	father_name = fields.Char(string="Father Name")
	cnic = fields.Char(string='CNIC',required=True)
	address = fields.Char(string="Address")
	mobile_number = fields.Char(string="Mobile Number",required=True)
	email = fields.Char(string="Email",required=True)
	app_city_id= fields.Many2one("ecube.city",string="City",required=True)
	student_form = fields.Many2one("ecube.res.partner",string="Student Form")
	nationality = fields.Char(string="Nationality")
	gender = fields.Selection([
	('male','Male'),
	('female','Female')], string="Gender")

	app_course_id = fields.Many2one("burhan.course",string="Apply Course",required=True)
	app_campus_id = fields.Many2one("burhan.campus",string="Apply Campus",required=True)
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


	
		

	@api.model
	def create(self,val):
		record = super(ApplicationForm, self).create(val)
		record.create_student_form()
		return record

	def write(self,val):

		record = super(ApplicationForm, self).write(val)
		# self.create_student_form()
		return record

	def create_student_form(self):
		student_form = self.env['ecube.res.partner']
		new_record_create_id = student_form.create({
			'name' : self.applicant_name,
			'father_name' : self.father_name,
			'cnic' : self.cnic,
			'mobile_number' : self.mobile_number,
			'address' : self.address,
			'email' : self.email,
			'city' : self.app_city_id.id,
			'nationality' : self.nationality,
			'gender' : self.gender,
			'course' : self.app_course_id.id,
			'campus' : self.app_campus_id.id,
			'date' : self.date,})
		
		print (new_record_create_id)
		self.student_form = new_record_create_id.id


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


