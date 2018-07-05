from django.conf.urls import url
from . import views

app_name ='galery_project'

urlpatterns = [
    url(r'^$', views.photo_upload, name='photo_upload'),
    url(r'^photo_list$', views.photo_list, name='photo_list'),
]