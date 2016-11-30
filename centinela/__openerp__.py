# -*- coding: utf-8 -*-
# © 2015 Eficent Business and IT Consulting Services S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

{
    'name': 'Centinela',
    'summary': 'Centinela',
    'version': '9.0.1.0.0',
    'category': 'Generic Modules',
    'author': (
        'Jarsa sistemas S.A de C.V. ,'
        'Odoo Community Association (OCA)'),
    'website': 'https://www.odoo-community.org',
    'license': 'LGPL-3',
    'depends': ['sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/centinel_quotation_view.xml',
        'views/centinel_service_view.xml',
        'views/centinel_group_view.xml',
        'views/centinel_workshift_view.xml',
        'views/centinel_subgroup_view.xml',
        'views/centinel_stand_view.xml',
        'views/centinel_standar_cost_view.xml',
        'views/centinel_rol_view.xml',
        'views/centinel_vacancy_view.xml',
        'views/centinel_activity_view.xml',
        'views/centinel_course_view.xml',
        'views/centinel_test_view.xml',
        'views/centinel_views.xml',
    ],
    'installable': True,
    'active': True
}
