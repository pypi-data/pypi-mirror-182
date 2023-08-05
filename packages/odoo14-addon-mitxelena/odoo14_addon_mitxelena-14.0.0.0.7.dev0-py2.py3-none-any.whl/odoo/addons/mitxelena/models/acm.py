from odoo import models, fields
from odoo.tools.translate import _

class acm(models.Model):
    _name = 'mitxelena.acm'
    _description = 'ACM management for Mitxelena'

    acm_code = fields.Char('Código ACM')
    date = fields.Date('Fecha')
    description = fields.Text('Descripción incidencia')
    status = fields.Selection([
        ('pendent', 'Pendiente'),
        ('delivered','Entregado'),
        ('refused', 'Rechazado')], string='Status')
    verified = fields.Boolean('Verificado')
    origin = fields.Char('Origen (libre)')
    duration = fields.Char('Duración (tiempo)')
    finish_date = fields.Date('Finalización (fecha)')
    period = fields.Date('Periodo (fecha)')
    real_duration = fields.Integer('Duración real')
    delay = fields.Integer('Retraso')
    #ncr_code = fields.Many2one(comodel_name='mitxelena_ncr', string='Código NCR')

