# -*- coding: utf-8 -*-
# © <2016> <Jarsa Sistemas, S.A. de C.V.>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class CentinelGroup(models.Model):
    _name = 'centinel.group'
    _description = 'Groups for service'

    name = fields.Char()
    service_id = fields.Many2one(
        'centinel.service')
    workshift_ids = fields.One2many(
        'centinel.workshift',
        'group_id',
        string='Workshifts')
