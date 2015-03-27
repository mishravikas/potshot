from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app.views.index'),
    url(r'^archive/$', 'app.views.archive'),
    url(r'^subscribe/$', 'app.views.subscribe'),
    url(r'^(\d+)/$', 'app.views.comic'),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
