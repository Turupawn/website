from __future__ import absolute_import

from rest_framework import filters, generics, permissions
from rest_framework.response import Response
from django.http import JsonResponse

from ingame_api.forms import (StatForm)
from django.shortcuts import get_object_or_404, redirect, render

from ingame_api import models, serializers

class GetStatsView(generics.GenericAPIView):

    def get_queryset(self):
        return models.Stat.objects.all()

    def get(self, request):
        serializer = serializers.StatSerializer(self.get_queryset(), many = True)
        return Response(serializer.data)

class SetStatView(generics.GenericAPIView):

    def get(self, request, stat_id, value):
        return JsonResponse({'message':'stat was set'})

class GetStatView(generics.GenericAPIView):

    def get(self, request, username, stat_id):
        return JsonResponse({'value': 75,
                              'stat':{'id': 54, 'type': "INT", 'name': "best score", 'increment_only': True,
                              'max_change': 0, 'min_change': 0, 'max_value': 100, 'window': 0,
                              'default_value': 0, 'aggregated': 0}})

def submit_stat(request):
    form = StatForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        stat = form.save()

        redirect_url = request.build_absolute_uri(reverse("api_stat_add"))

        LOGGER.info('Stat submitted, redirecting to %s', redirect_url)
        return redirect(redirect_url)
    return render(request, 'ingame_api/submit_stat.html', {'form': form})
