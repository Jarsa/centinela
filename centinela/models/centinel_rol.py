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
    description = fields.Char()
    partners = fields.Char(
        string='Has partners?')
    customers = fields.Char(
        string='With customers?')
    frecuent_problems = fields.Char()
    negative_experience = fields.Char(
            string='Negative experiences with'
                   'the previous service')
    plant_risk = fields.Char()
    crimen_risk = fields.Char()
    resources_risk = fields.Char()
    equipment = fields.Char()
    economic = fields.Char()
    task_complexity = fields.Char()
    confidential_info = fields.Char()
    relationship_hability = fields.Char()
    security_risk = fields.Char()
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
    vacancy_ids = fields.One2many(
        string='Vacancy')
