from django.urls import path

from .views import trails, filtered_trails, content_based_recommendations_view, createTrail, updateTrail, deleteTrail

urlpatterns = [
    path("", trails, name="trails"),
    path("filtered-trials/", filtered_trails, name="trails-f"),
    path("trail/<str:pk>/", content_based_recommendations_view, name="trails-r"),
    path("create-trail/", createTrail, name="create-trail"),
    path("update-trail/<str:pk>/", updateTrail, name="update-trail"),
    path("delete-trail/<str:pk>/", deleteTrail, name="delete-trail"),
]
