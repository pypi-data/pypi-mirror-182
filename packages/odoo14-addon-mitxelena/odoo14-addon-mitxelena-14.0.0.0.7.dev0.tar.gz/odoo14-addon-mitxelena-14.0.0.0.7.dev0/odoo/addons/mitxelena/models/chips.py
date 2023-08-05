# -*- coding: utf-8 -*-
from odoo import models, fields

class chips(models.Model):
    _name = 'mitxelena.chips'
    _description = 'Chips management for Mitxelena'

    name = fields.Char('Saco')
    order_number =  fields.Many2one(comodel_name='sale.order', string='Nº pedido cliente')
    reference = fields.Many2one(comodel_name='product.template', string='Referencia')
    material = fields.Many2one(comodel_name='product.template', string='Código de material de la viruta (Nuance AD)')
    bag_number = fields.Char('Nº Saco')
    opening_date = fields.Date('Fecha de apertura')
    collection_date = fields.Date('Fecha de recogida')
    work_order = fields.Many2one(comodel_name='mrp.production', string='OF')
    machine = fields.Many2one(comodel_name='mrp.workcenter', string='Máquina')
    operator = fields.Many2one(comodel_name='hr.employee', string='Operario')
    weight = fields.Float('Peso')
    number = fields.Char('Nº')
