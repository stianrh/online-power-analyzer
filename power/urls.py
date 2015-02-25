from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'power.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^$', 'measure.views.index', name='index'),
	url(r'^measure/(?P<num>\d+)/$', 'measure.views.measure', name='measure'),
	url(r'^measure/(?P<num>\d+)/start$', 'measure.views.start', name='start'),
	url(r'^measure/(?P<num>\d+)/image$', 'measure.views.get_image', name='get_image'),
	url(r'^flash/$', 'flash.views.index', name='flash_index'),
	url(r'^flash/compile/$', 'flash.views.compile', name='flash_compile'),
)
