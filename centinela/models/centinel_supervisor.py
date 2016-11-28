# -*- coding: utf-8 -*-
# © <2016> <Jarsa Sistemas, S.A. de C.V.>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models


class CentinelSupervisor(models.Model):
    _name = 'centinel.supervisor'
    _description = 'Supervisor model'

    date = fields.Datetime(readonly=True)
    customer_type = fields.Char(readonly=True)
    location = fields.Char(readonly=True)
    latitude = fields.Float(readonly=True)
    longitude = fields.Float(readonly=True)
    address = fields.Char(readonly=True)
    state = fields.Selection([
        ('suspect', 'Suspect'),
        ('prospect', 'Prospect'),
        ('pipeline', 'Pipeline'),
        ('forecast', 'Forecast'),
        ('won', 'Won'),
        ('lost', 'Lost'),
        ], readonly=True)
    recruitment_zone = fields.Selection([
        ('10_min', '10 minutes from distance'),
        ('30_min', 'A half of hour from distance'),
        ('3_km', '3 km from distance'),
        ], readonly=True)
    vacancy_ids = fields.One2many(
        'centinel.vacancy',
        'supervisor_id',
        string='Vacancy')
    customer_id = fields.Many2one(
        'res.partner',
        string='Customer',
        domain=[('customer', '=', 'True')])
    quotation_id = fields.Many2one(
        'centinel.quotation',
        string='Quotation')

    @api.onchange('quotation_id')
    def on_change_quotation(self):
        for rec in self:
            rec.date = rec.quotation_id.date
            rec.state = rec.quotation_id.state
            rec.customer_type = rec.quotation_id.customer_type
            rec.location = rec.quotation_id.location
            rec.latitude = rec.quotation_id.latitude
            rec.longitude = rec.quotation_id.longitude
            rec.address = rec.quotation_id.address
            rec.recruitment_zone = rec.quotation_id.recruitment_zone
            for stand in rec.quotation_id.stand_ids:
                if stand.service_ids:
                    for service in stand.service_ids:
                        for group in service.group_ids:
                            for wf in group.workshift_ids:
                                for sg in wf.subgroup_ids:
                                    for rol in sg.rol_id:
                                        for vac in rol.vacancy_ids:
                                            rec.vacancy_ids += vac
