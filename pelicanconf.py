#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""Settings for pelican."""

AUTHOR = 'Huashuai Qu'
SITENAME = 'Huashuai Qu'
SITEURL = 'http://www.quhuashuai.com'
TIMEZONE = 'UTC'

DEFAULT_CATEGORY = 'Uncategorized'
DATE_FORMAT = {
        'en': '%d %m %Y'
        }
DEFAULT_DATE_FORMAT = '%d %m %Y'

FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

# =============
# URL settings
# =============
ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = '%spages/{slug}.html'

# ===========
# Pagination
# ===========
WITH_PAGINATION = True
DEFAULT_PAGINATION = 10

# =================
# Ordering content
# =================
REVERSE_ARCHIVE_ORDER = True

# This can also be the absolute path to a theme that you downloaded
# i.e. './themes/anothertheme/'
# THEME = 'tuxlite_tbs'
THEME = 'flasky'

# The folder ``images`` should be copied into the folder ``static`` when
# generating the output.
STATIC_PATHS = ['images', ]

# I like to have ``Archives`` in the main menu.
MENUITEMS = (
    ['Home', 'http://www.quhuashuai.com'],
    ['Blog', 'http://huashuai.github.io/blog/'],
    ('Archives', '{0}/archives.html'.format(SITEURL)),
    ('Wedding', 'http://huashuaixuanwedding.com'),
    ['Life', 'http://huashuailovexuan.com']
)

WITH_PAGINATION = True
DEFAULT_PAGINATION = 10
REVERSE_ARCHIVE_ORDER = True

# Uncomment what ever you want to use
#GOOGLE_ANALYTICS = 'XX-XXXXXXX-XX'
MAIL_USERNAME = 'quhuashuai'
MAIL_HOST = 'gmail.com'
DISQUS_SITENAME = 'gitqu'
GITHUB_URL = 'http://github.com/huashuai/'
TWITTER_USERNAME = 'huashuai'
LINKEDIN_URL = 'http://www.linkedin.com/in/huashuai/'

DISPLAY_PAGES_ON_MENU = True

FILES_TO_COPY = (('extra/robots.txt', 'robots.txt'),
                ('extra/favicon.ico', 'favicon.ico'),)

PLUGIN_PATH = '/Users/Huashuai/Work/WebDev/pelican-plugins'
PLUGINS=['sitemap',]

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}
