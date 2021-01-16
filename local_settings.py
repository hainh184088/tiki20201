# from tiki20201.settings import PROJECT_ROOT, SITE_ROOT
import os

DEBUG = True
TEMPLATE_DEBUG = True

DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        'OPTIONS' : {
            'options': '-c search_path=end_term,public'
        },
        "NAME": "end_term",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "127.0.0.1",
        "PORT": "5432"
    }
}
