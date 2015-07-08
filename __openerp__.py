# -*- coding: utf-8 -*-
{
    'name': "Website - Sticky Header",

    'summary': '',

    'description': """
Website - Sticky Header
=======================
 * Provide a sticky header for website. 
 * Based on the 'Odoo-transparent-navbar' module by Fl0rianFischer (https://github.com/Fl0rianFischer/Odoo-transparent-navbar).""",
    'author': "Florian Fischer & Vizucom Oy",
    'website': "http://www.bloopark.de",

    'category': 'Modal',
    'version': '1.0',

    'depends': [
        'base',
        'website'
    ],
    'data': [
        'views/navbar.xml'
    ],
}
