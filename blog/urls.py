from django.conf.urls import patterns, include, url
from blog.models import userData, content

urlpatterns = patterns('blog.views',
	url(r'^$', 'login'),
	url(r'^check/$','check'),
	url(r'^(?P<user_id>\d+)/(?P<content_id>\d+)/$', 'main'),
	url(r'^(?P<user_id>\d+)/$', 'main'),
	url(r'^(?P<user_id>\d+)/new/$','new'),
)
#(?P<poll_id>\d+)
