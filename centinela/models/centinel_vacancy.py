# -*- coding: utf-8 -*-
# © <2016> <Jarsa Sistemas, S.A. de C.V.>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class CentinelVacancy(models.Model):
    _name = 'centinel.vacancy'
    _description = 'Vacancy for rol'

    name = fields.Char(string='Vacancy')
    rol_id = fields.Many2one(
        'centinel.rol',
        string='Rol')
    supervisor_id = fields.Many2one(
        'centinel.supervisor',
        string='Supervisor')
    activity = fields.Char(
        string='New model with selection widget')
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
    supervisor_id = fields.Many2one('centinel.supervisor')
