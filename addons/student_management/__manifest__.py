{
    'name': 'Student Management',
    'version': '1.0',
    'description': '',
    'depends': [
        'base'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/student_views.xml',
        'views/enrollment_views.xml',
        'views/course_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'student_management/static/src/js/dashboard.js',
            'student_management/static/src/xml/dashboard.xml',
            'https://cdn.jsdelivr.net/npm/chart.js'
        ],
    },
    'installable': True,
}