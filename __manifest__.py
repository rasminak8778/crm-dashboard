{
    'name': 'CRM Dashboard',
    'version': '17.0.1.0.0',
    'description': 'CRM Dashboard Management',
    'category': 'CRM/CRM Dashboard',
    'summary': 'Detailed Overview of CRM Dashboard',
    'installable': True,
    'application': True,
    'depends': [
        'crm',
        'sale',
    ],
    'data': [
        'views/crm_team_views.xml',
        'views/crm_dashboard_views.xml',
        # 'views/crm_graph_views.xml',

    ],
    'assets': {
        'web.assets_backend': [
            '/crm_dashboard/static/css/style.css',
            'crm_dashboard/static/src/js/dashboard.js',
            'crm_dashboard/static/src/xml/dashboard.xml',

        ],
    },
}
