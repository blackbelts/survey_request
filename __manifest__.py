# -*- coding: utf-8 -*-
{
    'name': "Protection survey",
    'summary': """Protectionr""",
    'description': """Protection """,
    'author': "Black Belts Egypt",
    'website': "www.blackbelts-egypt.com",
    'category': 'Motor',
    'version': '0.1',
    'license': 'AGPL-3',
    # any module necessary for this one to work correctly
    'depends': ['base','request','survey','crm'],

    # always loaded
    'data': [
        # 'security/security.xml',

        # 'views/requests.xml',
        'views/form_setup.xml',


        # 'views/arope_helpdesk.xml',
        # 'views/menu_item.xml',


    ],
    'qweb': [

        # "static/src/xml/broker_dash2.xml",

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    # 'css': ['/request/static/src/css/main.css'],
}
