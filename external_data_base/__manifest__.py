# -*- coding: utf-8 -*-
{
    'name': "External Data Framework",

    'summary': """
    Framework to build and manage import/export solutions""",

    'description': """
    Framework to build and manage import/export solutions.
    """,

    'author': "grzs",
    'website': "http://www.yourcompany.com",

    'category': 'Technical',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/external_data_source.xml',
        'views/external_data_object.xml',
        'views/external_data_field_mapping.xml',
        'views/external_data_rule.xml',
        'views/external_data_menus.xml',
        'actions/external_data_actions.xml',
    ],
}
