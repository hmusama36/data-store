# -*- coding: utf-8 -*- 
from odoo import models, fields, api
from odoo import models, fields 
from datetime import timedelta,datetime,date
import time
from odoo.exceptions import Warning, ValidationError

class OdooPrectice(models.Model): 
    _name = 'odoo.prectice' 
    _description = 'Odoo Prectice'
    # _rec_name = 'name'



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
    # arel_id2        = fields.Many2one('odoo.prectice.many2one',string="Many2one2")
    # link_form       = fields.Many2one('odoo.form',string="Link Form")
    aref            = fields.Reference([('res.partner', 'Nayyab')],string="Reference")
    afloat3         = fields.Float(digits=lambda cr: (5, 5),string="Float Digits lambda")
    aselection      = fields.Selection([('a', 'Rana'),('b', 'Rizwan'),('c', 'Ghani')],string="Selection")
    star            = fields.Selection([('0', 'Very Low'),('1', 'Low'),('2', 'Normal'),('3', 'High'),('4', 'Very High'),('5', 'Very Low') ], default='0')
    tree_link_id    = fields.One2many('odoo.prectice.tree','tree_link')

    stages = fields.Selection([
        ('draft', 'Draft'),
        ('approval', 'Approve'),
        ],default='draft',)

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
    def unlink(self):
        for x in self:
            if x.stages == "approval":
                raise  ValidationError('Cannot Delete Record')
    
        return super(OdooPrectice,self).unlink()


# class OdooPrecticeMany2one(models.Model): 
#     _name = 'odoo.prectice.many2one' 

#      name = fields.Char(string="Name")


class OdooPrecticeTree(models.Model):
    _name='odoo.prectice.tree'


    name = fields.Char(string='Name')
    rate = fields.Char(string='Rate')
    size = fields.Char(string='Size')
    abin2= fields.Binary(string="Image")
    payments=fields.Char(string='Payments')     
    tree_link=fields.Many2one('odoo.prectice')
