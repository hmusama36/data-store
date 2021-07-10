# -*- coding: utf-8 -*- 
from odoo import models, fields, api
from odoo import models, fields 
from datetime import timedelta,datetime,date
import time
from odoo.exceptions import Warning, ValidationError

class OdooPrectice(models.Model): 
    _name = 'odoo.prectice' 
    _description = 'Odoo Prectice'
    _rec_name = 'name'

    atext           = fields.Text(string="Text")
    anhtml          = fields.Html(string='Html')
    abin            = fields.Binary(string="Binary")
    anint           = fields.Integer(string='Integer')
    adate           = fields.Date(string="Date Simple")
    adate3          = fields.Datetime(string="Date Time")
    afloat          = fields.Float(string='Float Simple')
    abin3           = fields.Binary(string="Binary Image")
    abin2           = fields.Binary(string="Binary Image")
    computed_total  = fields.Float(compute='compute_total')
    name            = fields.Char(string='Char',required=True)
    sr_no           = fields.Char(readonly=True)
    abool           = fields.Boolean(string='Boolean',default=True)
    arel_id         = fields.Many2one('res.partner',string="Many2one")
    afloat2         = fields.Float(string='Float Digits',digits=(5,5))
    arel_ids        = fields.Many2many('res.partner',string="Many2many")
    adate2          = fields.Date(string="Date Today",default=date.today())
    arel_id2        = fields.Many2one('odoo.prectice.many2one',string="Many2one2")
    link_form       = fields.Many2one('odoo.form',string="Link Form")
    aref            = fields.Reference([('res.partner', 'Nayyab')],string="Reference")
    afloat3         = fields.Float(digits=lambda cr: (5, 5),string="Float Digits lambda")
    aselection      = fields.Selection([('a', 'Rana'),('b', 'Rizwan'),('c', 'Ghani')],string="Selection")
    star            = fields.Selection([('0', 'Very Low'),('1', 'Low'),('2', 'Normal'),('3', 'High'),('4', 'Very High'),('5', 'Very Low') ], default='0')
    tree_link_id    = fields.One2many('odoo.prectice.tree','tree_link')
    stages = fields.Selection([
        ('draft', 'Draft'),
        ('approval', 'Approve'),
        ],default='draft',)

    def compute_total(self):
        self.computed_total = self.afloat + self.afloat2

    @api.multi
    def draft(self):
        self.stages = 'draft'
    
    @api.multi 
    def duplicate(self):
        new_form = self.copy().id
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'odoo.prectice',
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'current',
            'res_id': new_form,
        }
    
    @api.multi
    def new_form(self):

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'odoo.prectice',
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'new',
        }

    @api.multi
    def pop_up(self):

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'odoo.prectice.popup',
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'new',
        }

    @api.multi
    def del_form(self):
        if self.stages == "draft":
            return super(OdooPrectice,self).unlink()        

    @api.multi
    def approve(self):
        self.stages = 'approval'

    @api.multi
    def unlink(self):
        for x in self:
            if x.stages == "approval":
                raise  ValidationError('Cannot Delete Record')
    
        return super(OdooPrectice,self).unlink()


    @api.model
    def create(self,vals):
        vals['sr_no'] = self.env['ir.sequence'].next_by_code('no.seq_odoo_prectice')
        new_record = super(OdooPrectice,self).create(vals)
        
        return new_record 


    @api.multi
    def value(self):
        # if not self.afloat: 
        self.afloat = self.afloat2 * 2

    @api.multi
    def create_form(self):
        if self.aref:
            new_record = self.env['odoo.form']
            form = new_record.create({
                'name'      : self.name,
                'anint'     : self.anint,
                'adate'     : self.adate,
                'sr_no'     : self.sr_no,
                'atext'     : self.atext,
                'afloat'    : self.afloat,
                'adate2'    : self.adate2,
                'adate3'    : self.adate3,
                'afloat2'   : self.afloat2,
                'afloat3'   : self.afloat3,
                'aref'      : self.aref.name,
                'aselection': self.aselection,
                'arel_id'   : self.arel_id.name,
                'arel_ids'  : self.arel_ids.name,
                'arel_id2'  : self.arel_id2.name,
                })
            self.link_form = new_record.id
            
            return form
        
        else:
            raise  ValidationError('Plz add Reference')




class OdooPrecticeMany2one(models.Model): 
    _name = 'odoo.prectice.many2one' 

    name = fields.Char(string="Name")


class OdooPrecticeTree(models.Model):
    _name='odoo.prectice.tree'


    name = fields.Char(string='Name')
    rate = fields.Char(string='Rate')
    size = fields.Char(string='Size')
    abin2= fields.Binary(string="Image")
    payments=fields.Char(string='Payments')     
    meb_no = fields.Char(string='Membership No')
    tree_link=fields.Many2one('odoo.prectice')


class OdooPrecticePOPUP(models.Model): 
    _name = 'odoo.prectice.popup' 




################################### I don't understand these fields #############################
# comodel_name: name of the opposite model
# relation: relational table name
# columns1: relational table left column name (reference to record in current table)
# columns2: relational table right column name (reference to record in comodel_name table)

    # arel_ids2 = fields.Many2many(comodel_name='res.partner',
 #                            relation='table_name',
 #                            column1='col_name',
 #                            column2='other_col_name')

    ####### inverse_name: relational column of the opposite model
    # arel_ids = fields.One2many('res.users', inverse_name='rel_id')

################ comodel_name: name of the opposite model ########
# delegate: set it to True to make fields of the target model accessible from the current model (corresponds to _inherits)

    # arel_id2 = fields.Many2one(comodel_name='res.users', delegate=True)
    
######## For use in odoo orginal Module  _inherit #########################

    # aselection2 = fields.Selection(selection_add=[('a', 'A')])

    # name2     = fields.Char(default=a_fun)


    # def a_fun(self):
 #          return self.do_something()



######################### New Form Create with button #########################

class OdooFrom(models.Model): 
    _name = 'odoo.form' 
    _description = 'Odoo Form'
    _rec_name = 'sr_no'


    # anhtml          = fields.Html(string='Html',readonly=True)
    # abin            = fields.Binary(string="Binary",readonly=True)
    # abool           = fields.Boolean(string='Boolean',default=True)
    atext           = fields.Text(string="Text",readonly=True)
    anint           = fields.Integer(string='Integer',readonly=True)
    adate           = fields.Date(string="Date Simple",readonly=True)
    adate3          = fields.Datetime(string="Date Time",readonly=True)
    afloat          = fields.Float(string='Float Simple',readonly=True)
    abin3           = fields.Binary(string="Binary Image",readonly=True)
    abin2           = fields.Binary(string="Binary Image",readonly=True)
    name            = fields.Char(string='Char',readonly=True)
    sr_no           = fields.Char(string="Sr No",readonly=True)
    arel_id         = fields.Char(string="Many2one",readonly=True)
    afloat2         = fields.Float(string='Float Digits',digits=(5,5),readonly=True)
    arel_ids        = fields.Char(string="Many2many",readonly=True)
    adate2          = fields.Date(string="Date Today",default=date.today(),readonly=True)
    arel_id2        = fields.Char(string="Many2one2",readonly=True)
    aref            = fields.Char(string="Reference",readonly=True)
    afloat3         = fields.Float(digits=lambda cr: (5, 5),string="Float Digits lambda",readonly=True)
    aselection      = fields.Selection([('a', 'Rana'),('b', 'Rizwan'),('c', 'Ghani')],string="Selection",readonly=True)
    star            = fields.Selection([('0', 'Very Low'),('1', 'Low'),('2', 'Normal'),('3', 'High'),('4', 'Very High'),('5', 'Very Low') ], default='0',readonly=True)
    # tree_link_id    = fields.One2many('odoo.prectice.tree','tree_link')


