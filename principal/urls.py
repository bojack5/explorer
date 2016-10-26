from principal import views
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add_comentario/$', views.add_comentario, name='comentario'),
    url(r'^admin/', admin.site.urls),
]
