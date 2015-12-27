from django.conf.urls import url

from junaApp.views.index_views import index
from junaApp.views.asema_views import asema
from junaApp.views.lataus_views import lataus
from junaApp.views.juna_views import juna
from junaApp.views.jselaus_views import jselaus

urlpatterns = [
    url(r'^$',index, name="index"),
    url(r'^asema', asema, name="asema"),
    url(r'^lataus', lataus, name="lataus"),
    url(r'^juna', juna, name="juna"),
    url(r'^jselaus', jselaus, name="jselaus")
]
