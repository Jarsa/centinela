# -*- coding: utf-8 -*-
# © <2016> <Jarsa Sistemas, S.A. de C.V.>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class CentinelAptitude(models.Model):
    _name = 'centinel.aptitude'
    _description = 'Requested aptitudes'

    required_effort = fields.Char()
    complexity = fields.Selection([
        ('chubby', 'Chubby'),
        ('skinny', 'Skinny'),
        ('short', 'Short'),
        ('tall', 'Tall')])
    sex = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')])
    age = fields.Float()
    mental_concentration = fields.Char()
    basic_knowdlege = fields.Char()
    experiency = fields.Char()
    criteria = fields.Char()
    hability = fields.Char()
    scolarship_level = fields.Selection([
        ('primaria', 'Primaria'),
        ('secundaria', 'Secundaria'),
        ('preparatoria', 'Preparatoria'),
        ('no_importa', 'No importa')])
    rol_id = fields.Many2one(
        'centinel.rol')
