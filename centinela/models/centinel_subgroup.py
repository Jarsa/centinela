# -*- coding: utf-8 -*-
# © <2016> <Jarsa Sistemas, S.A. de C.V.>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class CentinelSubgroup(models.Model):
    _name = 'centinel.subgroup'
    _description = 'Subgroups from service'

    service_id = fields.Many2one(
        'centinel.service')
    name = fields.Char()
    rol = fields.Char()
    start_date = fields.Datetime()
    end_date = fields.Datetime()
