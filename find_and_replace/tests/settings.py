#
# settings for unittest
#
print("\n *** use unittest settings: %r" % __file__)

import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TEST_USER_NAME="test"
TEST_USER_PASS="12345678"

ROOT_URLCONF="find_and_replace.tests.urls"


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.common.CommonMiddleware',

    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',

    #'django_tools.middlewares.QueryLogMiddleware.QueryLogMiddleware',
)
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.i18n",
    "django.core.context_processors.debug",
    "django.core.context_processors.request",
    "django.core.context_processors.media",
    'django.core.context_processors.csrf',
    "django.core.context_processors.tz",
    "sekizai.context_processors.sekizai",
    "django.core.context_processors.static",
    "cms.context_processors.media",
    "cms.context_processors.cms_settings",
)

LANGUAGE_CODE = "en"
LANGUAGES = [
    ('en', 'English'),
    ('de', 'German'),
]
SECRET_KEY = 'unittests-fake-key'

PASSWORD_HASHERS = [ # Speeding up the tests
    'django.contrib.auth.hashers.MD5PasswordHasher',
]

SITE_ID = 1

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = '/media/'


def _temp_db_name():
    import tempfile
    filepath = os.path.join(tempfile.gettempdir(), "find_and_replace_tests.db")
    print(" *** use SQLite file: %r\n" % filepath)
    return filepath


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': ':memory:',
        'NAME': _temp_db_name(),
    }
}
del(_temp_db_name)


DEBUG=True
TEMPLATE_DEBUG=True

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.messages',

    'cms',
    'mptt',
    'menus',
    'sekizai',
    'djangocms_text_ckeditor',

    'find_and_replace',
]

MIGRATION_MODULES = {
    'cms': 'cms.migrations_django', # only for django CMS 3.0
    'menus': 'menus.migrations_django',
}

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "tests", "test_templates"),
)
CMS_TEMPLATES = (
    ('test_template.html', 'test template'),
)