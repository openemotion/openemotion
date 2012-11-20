from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('chat.views',
    url(r'^$', 'index'),
    url(r'^conversations/$', 'conversations'),
    url(r'^conversations/(?P<conversation_id>\d+)/$', 'conversation_details'),
    url(r'^conversations/(?P<conversation_id>\d+)/(?P<slug>[^/]+)/$', 'conversation_details'),
    url(r'^users/(?P<username>[^/]+)/$', 'user_details'),
    url(r'^terms/$', 'terms'),
    url(r'^faq/$', 'faq'),
    url(r'^contact/$', 'contact'),
)

urlpatterns += patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
