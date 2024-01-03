from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import is_valid_path

from .forms import TrailForm
from .models import Trail
from .utils import paginateTrails, searchTrails


# Create your views here.
def trails(request):
    trails, search_query = searchTrails(request)
    custom_range, trails = paginateTrails(request, trails, 6)
    context = {
        "trails": trails,
        "search_query": search_query,
        "custom_range": custom_range,
    }
    return render(request, "trails/trails.html", context)


def trail(request, pk):
    trailObj = Trail.objects.get(id=pk)
    return render(request, "trails/single-trail.html", {"trail": trailObj})


@login_required(login_url="login")
def createTrail(request):
    form = TrailForm()

    if request.method == "POST":
        form = TrailForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("trails")

    context = {"form": form}
    return render(request, "trails/trail_form.html", context)


@login_required(login_url="login")
def updateTrail(request, pk):
    trail = Trail.objects.get(id=pk)
    form = TrailForm(instance=trail)

    if request.method == "POST":
        form = TrailForm(request.POST, request.FILES, instance=trail)
        if form.is_valid():
            form.save()
            return redirect("trails")

    context = {"form": form}
    return render(request, "trails/trail_form.html", context)


@login_required(login_url="login")
def deleteTrail(request, pk):
    trail = Trail.objects.get(id=pk)

    if request.method == "POST":
        trail.delete()
        return redirect("trails")

    context = {"object": trail}
    return render(request, "trails/delete_template.html", context)
