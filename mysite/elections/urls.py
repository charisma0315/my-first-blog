from django.conf.urls import url
from . import views
#담당자
urlpatterns = [
	url(r'^$', views.index),

]