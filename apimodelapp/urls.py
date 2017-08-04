#!/usr/bin/env python
# coding:utf-8
from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r"", views.api_model, name="api_model"),#model/$
]