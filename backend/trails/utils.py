from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q

from .models import Trail


def paginateTrails(request, trails, results):
    page = request.GET.get("page")
    paginator = Paginator(trails, results)

    try:
        trails = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        trails = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        trails = paginator.page(page)

    leftIndex = int(page) - 4

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = int(page) + 5

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, trails


def searchTrails(request):
    search_query = ""

    if request.GET.get("search_query"):
        search_query = request.GET.get("search_query")

    trails = Trail.objects.filter(
        Q(name__icontains=search_query)
        | Q(city__icontains=search_query)
        | Q(region__icontains=search_query)
    )

    return trails, search_query
