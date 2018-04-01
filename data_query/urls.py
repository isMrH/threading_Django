from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$',views.dataquery,name='dataquery'),
    url(r'^selectlist$',views.selectlist,name='selectlist'),

]