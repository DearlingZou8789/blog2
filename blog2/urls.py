from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog2test/show_authors$','blog2test.views.show_authors'),
    url(r'^blog2test/show_books$','blog2test.views.show_books'),
    url(r'^blog2test/register$','blog2test.views.register'),
    url(r'^blog2test/index$','blog2test.views.index'),
)
