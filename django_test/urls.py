from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_test.views.home', name='home'),
	    (r'^articles/', include('article.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
