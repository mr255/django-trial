from django.conf.urls import url # possible error here, possible style update
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
	url('relative/', views.relative, name='relative'),
	url('other/', views.other, name='other'),
]