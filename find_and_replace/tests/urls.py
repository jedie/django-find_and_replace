from cms.sitemaps import CMSSitemap
from django.conf.urls import url, include, patterns
from django.conf.urls.i18n import i18n_patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = i18n_patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('cms.urls')),
)

# # This is only needed when using runserver.
# if settings.DEBUG:
#     if 'debug_toolbar' in settings.INSTALLED_APPS:
#         import debug_toolbar
#         urlpatterns = patterns('',
#             url(r'^__debug__/', include(debug_toolbar.urls)),
#         ) + urlpatterns
#
#     urlpatterns = patterns('',
#         url(r'^media/(?P<path>.*)$', 'django.views.static.serve',  # NOQA
#             {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
#         ) + staticfiles_urlpatterns() + urlpatterns  # NOQA
