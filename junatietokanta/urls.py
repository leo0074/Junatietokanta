from django.conf.urls import include, url
from django.contrib import admin
from junaApp.views.login_views import kirjaudu


urlpatterns = [
    url(r'^junaApp/', include('junaApp.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login', kirjaudu, name='login')
]


