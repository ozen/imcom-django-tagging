from django.conf.urls import patterns, url
from tagging import views

urlpatterns = [
    url(r'^import-tags/$', views.import_tags, name='tagging_import_tags'),
]