# -*- coding: utf-8 -*-
# © <2016> <Jarsa Sistemas, S.A. de C.V.>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models


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
    vacancy = fields.Integer(
        string='How many vacancy'
        ' could have this role?')
    vacancy_ids = fields.One2many(
        'centinel.vacancy',
        'rol_id',
        string='Vacancy')

    @api.multi
    def create_vacancies(self, res):
        vacancy_obj = self.env['centinel.vacancy']
        i = 1
        while i <= res.vacancy:
            if len(vacancy_obj.search([]).ids) <= 0:
                    name = 1
            else:
                name = vacancy_obj.search([]).ids[-1] + 1
            vacancy_obj.create({
                'name': str(name),
                'rol_id': res.id,
                })
            i += 1

    @api.model
    def create(self, values):
        res = super(CentinelRol, self).create(values)
        res.create_vacancies(res)
        return res

    @api.multi
    def write(self, values):
        for rec in self:
            res = super(CentinelRol, self).write(values)
            rec.vacancy_ids.unlink()
            rec.create_vacancies(rec)
            return res
