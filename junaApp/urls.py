from django.conf.urls import url

from junaApp.views.index_views import index
from junaApp.views.asema_views import asema
from junaApp.views.lataus_views import lataus

urlpatterns = [
    url(r'^$',index, name="index"),
    url(r'^asema', asema, name="asema"),
    url(r'^lataus', lataus, name="lataus"),

]
