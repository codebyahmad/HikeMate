from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.RouteType)
class RouteTypeAdmin(admin.ModelAdmin):
  list_display = ('name', 'slug', 'created_at', 'updated_at')

@admin.register(models.Activity)
class ActivityAdmin(admin.ModelAdmin):
  list_display = ('name', 'slug', 'created_at', 'updated_at')

@admin.register(models.Feature)
class FeatureAdmin(admin.ModelAdmin):
  list_display = ('name', 'slug', 'created_at', 'updated_at')

@admin.register(models.Obstacle)
class ObstacleAdmin(admin.ModelAdmin):
  list_display = ('name', 'slug', 'created_at', 'updated_at')

@admin.register(models.Trail)
class TrailAdmin(admin.ModelAdmin):
  list_display = ('name', 'slug', 'city', 'region', 'review_count', 'avg_rating', 'popularity', 'created_at', 'updated_at')

@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
  list_display = ('trail', 'user', 'description', 'rating', 'created_at', 'updated_at')