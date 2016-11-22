# -*- coding: utf-8 -*-
# © <2016> <Jarsa Sistemas, S.A. de C.V.>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class CentinelSubgroup(models.Model):
    _name = 'centinel.subgroup'
    _description = 'Quotation from salesman'

    name = fields.Char()
    workshift_id = fields.Many2one(
        'centinel.workshift',
        string='Workshift')
    rol_id = fields.One2many(
        'centinel.rol',
        'workshift_id',
        string='Rol')
