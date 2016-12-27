from django.conf.urls import url
from django.contrib import admin

import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='myproject'),
    url(r'^admin/', admin.site.urls),
]
