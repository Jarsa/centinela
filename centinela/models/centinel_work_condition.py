# -*- coding: utf-8 -*-
# © <2016> <Jarsa Sistemas, S.A. de C.V.>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class CentinelWorkCondition(models.Model):
    _name = 'centinel.work.conditions'
    _description = 'Work description for quotation'

    description = fields.Char()
    with_partners = fields.Boolean(
        string='Has partners?')
    with_customers = fields.Boolean(
        string='With customers?')
    frecuent_problems = fields.Char()
    negative_experience = fields.Char(
            string='Negative experiences with'
                   'the previous service')
    plant_risk = fields.Char()
    crimen_risk = fields.Char()
    resources_risk = fields.Char()
