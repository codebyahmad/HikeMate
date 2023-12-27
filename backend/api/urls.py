from django.urls import path
from .views import TrailList, TrailDetail

app_name = 'api'

urlpatterns = [
  # Show all the data in our Database (Main Page)
  path('', TrailList.as_view(), name='listcreate'),
  # Show individual component or object in our Database
  path('<int:pk>/', TrailDetail.as_view(), name='detailcreate'),
]