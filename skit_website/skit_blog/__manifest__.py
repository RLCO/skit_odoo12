# -*- coding: utf-8 -*-

{
    'name': 'Skit Website Blog',
    'version': '1.1',
    'summary': 'Blog for webpage',
    'author': 'Srikesh Infotech',
    'license': "AGPL-3",
    'website': 'http://www.srikeshinfotech.com',
    'description': """
        """,
    'category': "Blog",
    'depends': ['website', 'website_blog', 'web', 'portal','skit_website_menu'],
    'data': [
        'views/blog.xml',
        'views/blog_view.xml',

    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
