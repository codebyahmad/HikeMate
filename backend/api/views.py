from rest_framework import generics
from .serializers import TrailSerializer
# from .models import Trail

# Create your views here.
class TrailList(generics.ListCreateAPIView):
  # queryset = Trail.trailobjects.all()
  # serializer_class = TrailSerializer
  pass

class TrailDetail(generics.RetrieveDestroyAPIView):
  pass