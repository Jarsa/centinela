# -*- coding: utf-8 -*-
# © <2016> <Jarsa Sistemas, S.A. de C.V.>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class CentinelService(models.Model):
    _name = 'centinel.service'
    _description = 'Description service from quiotation'

    service = fields.Char(
        string='Service name')
    mix = fields.Selection([
        ('12x12', '12 x 12'),
        ('12x24', '12 x 24'),
        ('24x48', '24 x 48'),
        ('24x24', '24 x 24'),
        ], default='12x12')
    turn = fields.Char()
    group_ids = fields.One2many(
        'centinel.group',
        'service_id',
        string='Subgroups')
    quotation_id = fields.Many2one(
        'centinel.quotation')
    stand_id = fields.Many2one(
        'centincel.stand')
