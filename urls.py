from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'wallets.views.home', name='home'),
    url(r'^wallet/(?P<uuid>.*?)$', 'wallets.views.wallet', name='wallet'),
    # url(r'^$', 'instawallet.views.home', name='home'),
    # url(r'^instawallet/', include('instawallet.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
