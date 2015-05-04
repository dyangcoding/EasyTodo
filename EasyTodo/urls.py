from django.conf.urls import include, url
from django.contrib import admin

from EasyTodoLib import urls as EasyTodoLibUrls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^todos/', include(EasyTodoLibUrls))
]
