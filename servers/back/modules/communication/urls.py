# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from modules.communication import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.list,
        name='list'
    ),

]
