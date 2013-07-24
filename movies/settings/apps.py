
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'djangoratings',
    'django.contrib.webdesign',
    'django.contrib.formtools',
    'django.contrib.humanize',
#    'django.contrib.gis',
    'django.contrib.comments',
]

INSTALLED_APPS += [
    'movies.apps.core',
]

INSTALLED_APPS += [
    'sorl.thumbnail',
    'debug_toolbar',
    'south',
    'annoying',
    'django_coverage',
    'compressor',
    'pinax.templatetags',
    'pinax.apps.account',
    'pinax.apps.signup_codes',
    'pinax.apps.waitinglist',
    'pinax_theme_bootstrap',
    'emailconfirmation',
    'django_forms_bootstrap',
    'ajax_select',
    'bootstrapform_too',
    'modelhelpers',
    'djangoratings'
]

INSTALLED_APPS_MORE = []
