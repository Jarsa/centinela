# -*- coding: utf-8 -*-
# © <2016> <Jarsa Sistemas, S.A. de C.V.>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class CentinelWorkshift(models.Model):
    _name = 'centinel.workshift'
    _description = 'workshift for groups'

    name = fields.Char()
    group_id = fields.Many2one(
        'centinel.group')
    subgroup_ids = fields.One2many(
        'centinel.subgroup',
        'workshift_id')
