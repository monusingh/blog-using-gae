from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    #('^$', 'django.views.generic.simple.direct_to_template',
    # {'template': 'home.html'}),
    
    ('^$','blog.views.index'),
    ('^about','blog.views.about'),
    ('^resume','blog.views.resume'),
    
    ('^home','blog.views.home'),
    ('^(\d+)/$', 'blog.views.post'),
    ('^add_comment/(\d+)/$', 'blog.views.add_comment'),
    ('^contact', 'blog.views.contact'),
    ('^Blog/$', 'blog.views.Blog'),
    ('^Blog/create_post/$', 'blog.views.create_post'),
    ('^admin/', include(admin.site.urls)),
    ('^accounts/', include('registration.urls')),
    
    
)
