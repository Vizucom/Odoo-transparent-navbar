# -*- coding: utf-8 -*-
{
    'name': "Website - Sticky Header",

    'summary': '',

    'description': """
Website - Sticky Header
=======================
 * Provide a sticky header with an easing animation for the website . 
 * Based on the 'Odoo-transparent-navbar' module by Fl0rianFischer (https://github.com/Fl0rianFischer/Odoo-transparent-navbar).""",
    'author': "Florian Fischer & Vizucom Oy",
    'website': "http://www.bloopark.de",

    'category': 'Modal',
    'version': '1.0',

    'depends': [
        'website'
    ],
    'data': [
        'views/sticky_header.xml'
    ],
}
