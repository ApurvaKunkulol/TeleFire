__author__ = 'LENOVO'

from django.conf.urls import url
from .import views

app_name = "decision_maker"
urlpatterns = [
    url(r'^$', views.CallUser.as_view(), name='dm_index')
]

