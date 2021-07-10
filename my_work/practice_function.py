import webbrowser
webbrowser.open('https://www.python.org' new=0,1,2)

for redirect to tab
https://www.codegrepper.com/code-examples/python/open+url+in+python


onchange use
@api.onchange('fname')
def _onchange_name(self):
     if self.fname: 
         self.name = str(self.fname)
@api.model    
def create(self, vals):
     if vals['fname']:
         vals['name'] = vals['fname']
     res = super(Demo, self).create(vals)        
     return res
@api.multi
def write(self, vals):
     if vals['name']:
         vals['name'] = vals['fname']
     res = super(Demo, self).write(vals)
     return res




	# @api.onchange('student_name')
	# def getdiff(self):
	# 	print "===========onchange=========="
	# 	self.student_name=self.name.student_name

sir haroon work

	@api.multi
	def write(self, vals):
		super(EcubeStudentData, self).write(vals)
		print "============write============="


	@api.model
	def create(self, vals):
		Res = super(EcubeStudentData,self).create(vals)
		print "================create============="
		return Res


	@api.multi
	def unlink(self):
		given = super(EcubeStudentData,self).unlink()
		print "==============delete==============="
		return given


	@api.multi
	def invoice(self):
		for rec in self:
			rec = 'Invoice'

		create_receipt = self.env['ecube.student.invoice'].create({
			'student_name': self.id,
			'total_amount': self.monthly_fee+self.admission_fee,
			'description':"Total Amount"})

		all_records = self.env['ecube.student.invoice'].search([('student_name','=',self.id)])
		print "==================================="
		for record in all_records:	
			print record
			print record.student_name.father_name
			print record.total_amount





total get value
	@api.onchange('tree_id')
	def gettotal(self):
		print "=============onchange.total=============="
		total = 0
		for lines in self.tree_id:
			total = total + lines.subtotal
		self.total = total



	@api.multi
	def new_form(self):
		print "======create button======"
		return {
			'type': 'ir.actions.act_window',
			'res_model': 'ecube.partner',
			'view_type': 'form',
			'view_mode': 'form',
			'target': 'new',
		}


	@api.multi 
	def duplicate(self):
		new_form = self.copy().id
		return {
			'type': 'ir.actions.act_window',
			'res_model': 'ecube.partner',
			'view_type': 'form',
			'view_mode': 'form',
			'target': 'new',
			# 'res_id': new_form,
		}

	@api.multi
	def draft(self):
		self.stages = 'draft'




  for raisee validation error if mail is not valid

  @api.onchange('email')
	def validate_mail(self):
	       if self.email:
	        match = re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", self.email)
	        if match == None:
	            raise ValidationError('Not a valid E-mail')


link of ottoman empire
	            https://www.dailymotion.com/video/x7x5pvb

link mavera https://www.giveme5.co/mavera-urdu-giveme5

github yasir
		https://github.com/khyasir







		server commands for github
		import os
import time
 
os.chdir('/home/odoo/Desktop/odoo10git')
os.system('git init')
os.system('git remote add origin https://github.com/khyasir/odoo-10')
os.system('git add *')
os.system('git status')
os.system('git commit -m "salllenuim work in bio machine"')
os.system('git push origin master')