from django.conf.urls import url, include
from django.contrib import admin

from core import views


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^fale-conosco/$', views.contact, name='contact'),
	url(r'^', include('courses.urls', namespace='courses')),
    url(r'^admin/', admin.site.urls),
]
