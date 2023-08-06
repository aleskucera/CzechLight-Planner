# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import debug_toolbar
from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin route
    path("", include("apps.authentication.urls")),  # Auth routes - login / register

    # ADD NEW Routes HERE
    path("", include("apps.nodes.urls")),
    path("", include("apps.connection.urls")),

    # Leave `Home.Urls` as last the last line
    path("", include("apps.home.urls"))
]
