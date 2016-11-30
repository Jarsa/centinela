# -*- coding: utf-8 -*-
# © <2016> <Jarsa Sistemas, S.A. de C.V.>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class CentinelVacancy(models.Model):
    _name = 'centinel.vacancy'
    _description = 'Vacancy for rol'

    name = fields.Char(string='Vacancy')
    activity_id = fields.Many2one(
        'centinel.activity',
        string='Activity',
        domain="[('active', '=', True)]")
    how_to = fields.Char()
    attachment = fields.Binary()
    origin_address = fields.Char()
    origin_latitude = fields.Char()
    origin_longitude = fields.Char()
    origin_hour = fields.Char()
    origin_day = fields.Datetime()
    destiny_address = fields.Char()
    destiny_latitude = fields.Char()
    destiny_longitude = fields.Char()
    destiny_hour = fields.Char()
    destiny_day = fields.Datetime()
    rol_id = fields.Many2one(
        'centinel.rol',
        string='Rol')
    quotation_id = fields.Many2one(
        'centinel.quotation',
        string='Supervisor')
    course_ids = fields.Many2many(
        'centinel.course',
        string='Courses')
    test_ids = fields.Many2many(
        'centinel.test',
        string='Tests')
    tool_ids = fields.Many2many(
        'product.product',
        string='Tools')
    weapon_ids = fields.Many2many(
        'product.product',
        string='Weapons')
