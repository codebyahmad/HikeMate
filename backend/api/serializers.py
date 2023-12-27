from rest_framework import serializers
from .models import RouteType, Activity, Feature, Obstacle

class TrailSerializer(serializers.ModelSerializer):
  pass
  # route_type = serializers.ChoiceField(choices=RouteType.objects.values_list('uid', 'name'))
  # activities = serializers.MultipleChoiceField(choices=Activity.objects.values_list('uid', 'name'))
  # features = serializers.MultipleChoiceField(choices=Feature.objects.values_list('uid', 'name'))
  # obstacles = serializers.MultipleChoiceField(choices=Obstacle.objects.values_list('uid', 'name'))

  # class Meta:
  #   model = Trail
  #   fields = ( 
  #     'name', 
  #     'slug',
  #     'overview', 
  #     'route_type', 
  #     'image_id',
  #     'city',
  #     'region',
  #     'country',
  #     'latitude',
  #     'longitude',
  #     'rating',
  #     'difficulty',
  #     'popularity',
  #     'season_start',
  #     'season_end',
  #     'length',
  #     'duration',
  #     'elevation_start',
  #     'elevation_gain',
  #     'elevation_max',
  #     'activities',
  #     'features',
  #     'obstacles',
  #     'author',
  #     'status'
  #   )