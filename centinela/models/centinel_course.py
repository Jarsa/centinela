# -*- coding: utf-8 -*-
# © <2016> <Jarsa Sistemas, S.A. de C.V.>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models


class CentinelCourse(models.Model):
    _name = 'centinel.course'
    _description = 'Courses for vacancy'

    name = fields.Char()
    active = fields.Boolean()
