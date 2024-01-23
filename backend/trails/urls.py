from django.urls import path

from . import views

urlpatterns = [
    path("", views.trails, name="trails"),
    path("filtered-trials/", views.content_based_recommendations_view, name="trails-r"),
    path("trail/<str:pk>/", views.trail, name="trail"),
    path("create-trail/", views.createTrail, name="create-trail"),
    path("update-trail/<str:pk>/", views.updateTrail, name="update-trail"),
    path("delete-trail/<str:pk>/", views.deleteTrail, name="delete-trail"),
]
