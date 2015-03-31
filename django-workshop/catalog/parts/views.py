from __future__ import absolute_import

from django.core import serializers
from django.http import (
    Http404,
    JsonResponse
)
from django.shortcuts import (
    render,
    get_object_or_404,
    get_list_or_404
)

from . import models


# Create your views here.

def by_slug(request, slug):
    pass


def by_year(request, year):
    if 2015 - int(year) < 0:
        raise Http404()

    # part = get_object_or_404(models.CarParts, year=year)
    parts = get_list_or_404(models.CarParts, year=year)

    # return render(request, 'by_year.html', {'year': year})
    return JsonResponse(
        {'part': serializers.serialize('json', parts)})


def index(request):
    if request.method == 'POST':
        part = models.CarParts()
        part.name = request.POST['name']
        part.slug = request.POST['slug']
        part.year = request.POST['year']

        part.save()

    return render(request, 'index.html')
