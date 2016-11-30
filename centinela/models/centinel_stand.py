# -*- coding: utf-8 -*-
# © <2016> <Jarsa Sistemas, S.A. de C.V.>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class CentinelStand(models.Model):
    _name = 'centinel.stand'
    _description = 'stand for services'

    name = fields.Char()
    service_ids = fields.One2many(
        'centinel.service',
        'stand_id',
        string='Service')
    quotation_id = fields.Many2one(
        'centinel.quotation',
        string='Quotation')
