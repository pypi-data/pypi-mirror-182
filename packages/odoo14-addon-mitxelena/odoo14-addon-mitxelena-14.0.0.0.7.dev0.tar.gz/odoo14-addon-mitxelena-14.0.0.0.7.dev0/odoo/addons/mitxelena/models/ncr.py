from odoo import models, fields, api, exceptions

class ncr(models.Model):
    _name = 'mitxelena.ncr'
    _description = 'NCR management for Mitxelena'

    ncr_code = fields.Char('Código NCR')    
    date = fields.Date('Fecha')
    customer = fields.Many2one(comodel_name='res.partner', string='Cliente')
    article_position = fields.Many2one(comodel_name='manufacturing.order', string='Posición de artículo')
    cause_type = fields.Selection([
        ('kanpo-bezeroa','Kanpo Bezeroa' ),
        ('kanpo-hornitzalea','Kanpo Hornitzalea'),
        ('barnefab10','Barne Fabrik. 10'), 
        ('barnefab11','Barne Fabrik. 11'), 
        ('barnefab20','Barne Fabrik. 20'), 
        ('barnefab40','Barne Fabrik. 40'),
        ('barnefab41','Barne Fabrik. 41'), 
        ('barnefab50','Barne Fabrik. 50'), 
        ('barnefab51','Barne Fabrik. 51'), 
        ('barnefab52','Barne Fabrik. 52'),
        ('barnefab61','Barne Fabrik. 61'), 
        ('barnefab62','Barne Fabrik. 62'), 
        ('barnefab64','Barne Fabrik. 64'), 
        ('barnefab65','Barne Fabrik. 65'),
        ('barnefab66','Barne Fabrik. 66'), 
        ('barnefab67','Barne Fabrik. 67'), 
        ('barnefab30','Barne Fabrik. 30'), 
        ('barnefab-ez-daki','Barne Fabrik. Ez dakigu'),
        ('barnefab-soldadura','Barne Fabrik. Soldadura'),
        ('barnefab-montajea','Barne Fabrik. Montajea'), 
        ('barnefab-zamalanak','Barne Fabrik. Zamalanak'),
        ('kudeaketa-arazoa','Kudeaketa arazoa'), 
        ('id-ta-traz','Identifikazioa eta trazabilitatea'), 
        ('harrera-kontrola','Harrera kontrola'),
        ('produktua-babestea','Produktua babestea'), 
        ('lanen-azken-ikusi','Lanen azken ikuskatzea'), 
        ('grua','Grua'), 
        ('giza-faktorea','Giza faktorea')], string='Tipo de causa')

    responsable = fields.Many2one(comodel_name='hr.employee', string='Responsable')
    other_responsable = fields.Many2one(comodel_name='hr.employee', string='Otros responsables')
    description = fields.Text('Descripción')
    status = fields.Selection([
        ('pendent', 'Pendiente'),
        ('delivered','Entregado'),
        ('refused', 'Rechazado')], string='Status')
    cost = fields.Float('Coste')
    reviewed = fields.Boolean('Revisado')
