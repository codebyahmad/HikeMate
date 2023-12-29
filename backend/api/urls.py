from django.urls import path
from .views import TrailList, TrailDetail

app_name = 'api'

urlpatterns = [
	path('', TrailList.as_view(), name='listcreate'),
	path('<str:pk>/', TrailDetail.as_view(), name='detailcreate'),
]