from django import forms
from django.forms import ModelForm, widgets

from .models import Trail


class TrailForm(ModelForm):
    class Meta:
        model = Trail
        fields = [
            "name",
            "slug",
            "overview",
            "route_type",
            "featured_image",
            "city",
            "region",
            "country",
            "latitude",
            "longitude",
            "difficulty",
            "popularity",
            "season_start",
            "season_end",
            "length",
            "duration",
            "elevation_start",
            "elevation_gain",
            "elevation_max",
            "activities",
            "features",
            "obstacles",
        ]

        widgets = {
            "activities": forms.CheckboxSelectMultiple(),
            "features": forms.CheckboxSelectMultiple(),
            "obstacles": forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(TrailForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "input"})

        # self.fields['name'].widget.attrs.update({'class':'input'})
        # self.fields['overview'].widget.attrs.update({'class':'input'})
