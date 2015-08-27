
#
# settings for unittest
#

print("\nuse unittest settings: %r\n" % __file__)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.request",
    "django.contrib.auth.context_processors.auth",
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',

    #'django_tools.middlewares.QueryLogMiddleware.QueryLogMiddleware',
)

LANGUAGE_CODE = "en"
LANGUAGES = (
    ("en","de"),
)
SECRET_KEY = 'unittests-fake-key'

PASSWORD_HASHERS = [ # Speeding up the tests
    'django.contrib.auth.hashers.MD5PasswordHasher',
]

SITE_ID = 1

ROOT_URLCONF="tests.urls"
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

DEBUG=True

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.sessions',

    'mptt',
    'cms',

    'find_and_replace.tests',
]

MIGRATION_MODULES = {
    'cms': 'cms.migrations_django', # only for django CMS 3.0
}