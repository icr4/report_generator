{
    'name': "Report Generator",
    'summary': "PDF Report Generator",
    'description': "This module permits to generate custom PDF reports basing on a PDF template instead of using Qweb or wkhtmltopdf.",
    'author': "Alessandro Gessa, Bootando",
    'website': "http://www.bootando.com",
    'category': 'Productivity',
    'version': '1.0',
    'application': False,
    'installable': True,
    'price': 139.99,
    'currency': 'EUR',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'mail'
    ],
    'images': ['static/images/thumbnail.png'],
    'data': [
        'security/ir_module_category.xml',
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        
        'menu/actions.xml',
        'menu/items.xml',
        
        'views/report_views.xml',
        'views/report_placeholder_views.xml',
        'views/report_placeholder_font_views.xml',
        'views/ir_actions_server_views.xml',
        
        'wizards/views/output_wizard_views.xml',
        'wizards/views/preview_wizard_views.xml'
    ],
    'assets': {
        'web.assets_backend': {
            "/report_generator/static/src/js/widget.js",
            "/report_generator/static/src/scss/modal.scss"
        },
        'web.assets_qweb': {
            "/report_generator/static/src/xml/widget_template.xml"
        },
    },
    'post_init_hook': 'post_init_hook'
}