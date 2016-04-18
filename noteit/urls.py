from django.conf.urls import patterns, include, url
from django.contrib import admin
from noteitid.views import HomeView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'noteit.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', HomeView.as_view(), name='index'),
    url(r'^admin/', include(admin.site.urls)),
)
