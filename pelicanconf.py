#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Andr\xe9s S\xe1nchez Garc\xeda'
SITENAME = u'SysAdmin Blog!'
SITEURL = ''
GITHUB_URL = 'http://github.com/asg1612'

PATH = 'content'

TIMEZONE = 'Europe/Madrid'

DEFAULT_LANG = u'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/asg1612'),
		 ('linkedin', 'https://www.linkedin.com/profile/view?id=23101412'),
		       ('github', GITHUB_URL),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
