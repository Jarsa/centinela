# -*- coding: utf-8 -*-
# © <2016> <Jarsa Sistemas, S.A. de C.V.>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models


class CentinelQuotation(models.Model):
    _name = 'centinel.quotation'
    _description = 'Quotation from salesman'

    name = fields.Char(
        string='Name')
    nbr_vacancies = fields.Integer(
        compute='_compute_nbr_vacancies',
        string='Vacancies')
    date = fields.Datetime(
        default=fields.Datetime.now)
    user_id = fields.Many2one(
        'res.partner',
        string='User')
    state = fields.Selection([
        ('suspect', 'Suspect'),
        ('prospect', 'Prospect'),
        ('pipeline', 'Pipeline'),
        ('forecast', 'Forecast'),
        ('won', 'Won'),
        ('lost', 'Lost'),
        ], default='prospect')
    customer_id = fields.Many2one(
        'res.partner',
        string='Customer',
        domain=[('customer', '=', 'True')])
    customer_type = fields.Char()
    location = fields.Char()
    latitude = fields.Float()
    longitude = fields.Float()
    address = fields.Char()
    recruitment_zone = fields.Selection([
        ('10_min', '10 minutes from distance'),
        ('30_min', 'A half of hour from distance'),
        ('3_km', '3 km from distance'),
        ], default='10_min')
    stand_ids = fields.One2many(
        'centinel.stand',
        'quotation_id',
        string='Stand')

    @api.model
    def create(self, values):
        quotation = super(CentinelQuotation, self).create(values)
        quotation.name = self.env['centinel.quotation'].search(
            []).ids[-1] + 1
        return quotation

    @api.depends('customer_id')
    def onchange_vacancies(self):
        for rec in self:
            rec.vacancy_ids = []
            for stand in rec.stand_ids:
                for service in stand.service_ids:
                    for group in service.group_ids:
                        for works in group.workshift_ids:
                            for sog in works.subgroup_ids:
                                for rol in sog.rol_id:
                                    for vac in rol.vacancy_ids:
                                        rec.vacancy_ids += vac

    @api.multi
    def quotation_vacancies(self):
        for rec in self:
            roles = (
                rec.stand_ids.service_ids.group_ids.
                workshift_ids.subgroup_ids.rol_ids)

            return {
                'name': 'Vacancies',
                'view_type': 'form',
                'view_mode': 'tree,form',
                'res_model': 'centinel.vacancy',
                'domain': [('rol_id', 'in', roles.ids)],
                'type': 'ir.actions.act_window'}

    @api.depends('stand_ids')
    def _compute_nbr_vacancies(self):
        for rec in self:
            vacancies = []
            roles = (
                rec.stand_ids.service_ids.group_ids.
                workshift_ids.subgroup_ids.rol_ids)
            for rol in roles:
                vacancies.extend(rol.vacancy_ids.ids)
            rec.nbr_vacancies = len(vacancies)
