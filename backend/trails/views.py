import pandas as pd
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

from .forms import TrailForm
from .models import Trail, Feature
from .utils import paginateTrails, searchTrails


# Create your views here.
def trails(request):
    # trails, search_query = searchTrails(request)
    # custom_range, trails = paginateTrails(request, trails, 6)
    trails = Trail.objects.all()
    features = Feature.objects.all()
    # p = request.GET.get('price_lte')
    # print(p)
    regions = trails.order_by('-region')
    unique_regions = set()
    length_max = trails.order_by('-length')[0].length
    length_min = trails.order_by('length')[0].length
    duration_max = trails.order_by('-duration')[0].duration
    duration_min = trails.order_by('duration')[0].duration
    for region in regions:
        unique_regions.add(region.region)
    context = {
        # "trails": trails,
        # "search_query": search_query,
        # "custom_range": custom_range,
        "features": features,
        "regions": unique_regions,
        "length_max": length_max,
        "length_min": length_min,
        "duration_max": duration_max,
        "duration_min": duration_min,
    }

    return render(request, "trails/trails.html", context)


def filtered_trails(request):
    length_max = request.GET.get('length_max')
    length_min = request.GET.get('length_min')
    duration_max = request.GET.get('duration_max')
    duration_min = request.GET.get('duration_min')
    region = request.GET.get('region')
    features = request.GET.get('features').split(',') if request.GET.get('features') else ()
    trails = Trail.objects.filter(region=region,
                                  length__range=(length_min, length_max),
                                  duration__range=(duration_min, duration_max),
                                  features__in=features).all()

    return render(request, "trails/trails.html", context={'trails': trails})


def get_content_based_recommendations(df, trail_name, cosine_sim, n):
    idx = df[df['name'] == trail_name].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:n + 1]  # Exclude the trail itself
    trail_indices = [i[0] for i in sim_scores]
    return df[['name', 'avg_rating']].iloc[trail_indices]


def content_based_recommendations_view(request):
    trail_name = request.GET.get('trail_name')
    num_of_trials = request.GET.get('num_of_trials')
    trails = Trail.objects.all()

    content_features = pd.DataFrame(
        trails.values('name', 'popularity', 'length', 'elevation_gain', 'avg_rating', 'difficulty'))

    content_features['combined_features'] = content_features.apply(
        lambda row: ' '.join(row.values.astype(str)), axis=1
    )

    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf_vectorizer.fit_transform(content_features['combined_features'])
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

    content_based_recommendations = get_content_based_recommendations(content_features, trail_name, cosine_sim,
                                                                      int(num_of_trials))

    trails = trails.filter(name__in=[v['name'] for i, v in content_based_recommendations.iterrows()])

    return render(request, "trails/filtered-trails.html", context={'trails': trails})


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
