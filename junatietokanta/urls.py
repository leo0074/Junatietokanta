from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^junaApp/', include('junaApp.urls')),
    url(r'^admin/', include(admin.site.urls)),
]


