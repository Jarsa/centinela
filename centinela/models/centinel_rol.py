# -*- coding: utf-8 -*-
# © <2016> <Jarsa Sistemas, S.A. de C.V.>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class CentinelRol(models.Model):
    _name = 'centinel.rol'
    _description = "Rol in service"

    name = fields.Char()
    workshift_id = fields.Many2one(
        'centinel.workshift')
    work_condition_ids = fields.One2many(
        'centinel.work.condition',
        'rol_id')
    responsability_ids = fields.One2many(
        'centinel.responsability',
        'rol_id')
    aptitude_ids = fields.One2many(
        'centinel.aptitude',
        'rol_id')
