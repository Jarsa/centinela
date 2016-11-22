# -*- coding: utf-8 -*-
# © <2016> <Jarsa Sistemas, S.A. de C.V.>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class CentinelStandarCost(models.Model):
    _name = 'centinel.standar.cost'
    _description = 'Standar cost of each employee'

    salary = fields.Float()
    bonus = fields.Float()
    vacation = fields.Float()
    social_security = fields.Float()
    infonavit = fields.Float()
    weapons_management = fields.Float()
    pc_management = fields.Float()
    bulletproof_vest = fields.Float()
    helmet = fields.Float()
    cellphone = fields.Float()
    total_standar_cost = fields.Float()
    product_id = fields.Many2one(
        'product.product',
        string='Uniform')
