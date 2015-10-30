from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'test_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	# this url comes by default:

    url(r'^admin/', include(admin.site.urls)),
	url(r'^$', 'blog.views.index'),
	url(r'^author/', 'blog.views.aboutme'),
    url(r'^(?P<slug>[\w\-]+)/$', 'blog.views.details'),	

)
