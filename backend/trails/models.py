import uuid

from django.contrib.auth.models import User
from django.db import models

# from users.models import Profile


# Create your models here.
class RouteType(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    slug = models.SlugField(max_length=50, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Activity(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    slug = models.SlugField(max_length=50, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Feature(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    slug = models.SlugField(max_length=50, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Obstacle(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    slug = models.SlugField(max_length=50, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Trail(models.Model):
    MONTH_CHOICES = (
        (1, "January"),
        (2, "February"),
        (3, "March"),
        (4, "April"),
        (5, "May"),
        (6, "June"),
        (7, "July"),
        (8, "August"),
        (9, "September"),
        (10, "October"),
        (11, "November"),
        (12, "December"),
    )

    # Basic trail information
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, null=False, blank=False)
    overview = models.TextField(null=True, blank=True)
    route_type = models.ForeignKey(
        RouteType, on_delete=models.SET_NULL, null=True, blank=True
    )
    featured_image = models.ImageField(null=True, blank=True, default="default.webp")

    # Location details
    city = models.CharField(max_length=50, null=False, blank=False)
    region = models.CharField(max_length=50, null=False, blank=False)
    country = models.CharField(max_length=50, null=False, blank=False)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    # Difficulty, rating and popularity
    difficulty = models.PositiveIntegerField(null=True, blank=True)
    review_count = models.PositiveIntegerField(default=0, null=True, blank=True)
    avg_rating = models.DecimalField(
        max_digits=2, decimal_places=1, null=True, blank=True
    )
    popularity = models.DecimalField(
        max_digits=6, decimal_places=4, null=True, blank=True
    )

    # Season information
    season_start = models.PositiveIntegerField(choices=MONTH_CHOICES)
    season_end = models.PositiveIntegerField(choices=MONTH_CHOICES)

    # Trail stats
    length = models.DecimalField(max_digits=8, decimal_places=3)
    duration = models.PositiveIntegerField()
    elevation_start = models.DecimalField(max_digits=9, decimal_places=4)
    elevation_gain = models.DecimalField(max_digits=9, decimal_places=4)
    elevation_max = models.DecimalField(max_digits=9, decimal_places=4)

    # activities, features, and obstacles
    activities = models.ManyToManyField(Activity, blank=True)
    features = models.ManyToManyField(Feature, blank=True)
    obstacles = models.ManyToManyField(Obstacle, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-created_at"]


class Review(models.Model):
    STAR_RATING = (
        (1, "1 Star"),
        (2, "2 Star"),
        (3, "3 Star"),
        (4, "4 Star"),
        (5, "5 Star"),
    )

    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    trail = models.ForeignKey(Trail, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    rating = models.PositiveIntegerField(choices=STAR_RATING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = [["user", "trail"]]

    def __str__(self):
        return f"{self.user}'s {self.rating}-star rating for {self.trail}"
