from rest_framework import serializers
from .models import RouteType, Activity, Feature, Obstacle, Trail, Review

class TrailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Trail
		fields = '__all__'