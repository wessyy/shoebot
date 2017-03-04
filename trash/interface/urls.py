from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.UserCreate.as_view(), name='user-add'),

	url(r'^completed/$', views.DetailView.as_view(), name='detail')
]