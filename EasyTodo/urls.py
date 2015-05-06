from django.conf.urls import include, url,patterns
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', admin.site.urls),
    url(r'^', include('EasyTodoLib.urls')),
    )

