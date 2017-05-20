from __future__ import absolute_import

import logging

from django.conf import settings
from rest_framework import filters, generics, permissions
from rest_framework.response import Response
from django.http import JsonResponse
from django.urls import reverse

from ingame_api.forms import (AchievementForm)
from django.shortcuts import get_object_or_404, redirect, render

from ingame_api import models, serializers


LOGGER = logging.getLogger(__name__)

#from ingame_api import models, serializers

class UnlockAchievementView(generics.GenericAPIView):

    def get(self, request, achievement_id):
        return JsonResponse({'message':'achievement was unlocked'})

class GetAchievementsView(generics.GenericAPIView):

    def get_queryset(self):
        return models.Achievement.objects.all()

    def get(self, request):
        serializer = serializers.AchievementSerializer(self.get_queryset(), many = True)
        return Response(serializer.data)

class GetUserAchievementView(generics.GenericAPIView):

    def get_queryset(self):
        return models.Achievement.objects.all()

    def get(self, request, username, achievement_id):
        serializer = serializers.AchievementSerializer(self.get_queryset(), many = True)
        return Response(serializer.data)

def submit_achievement(request):
    form = AchievementForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        achievement = form.save()

        redirect_url = request.build_absolute_uri(reverse("api_achievement_add"))

        LOGGER.info('Achievement submitted, redirecting to %s', redirect_url)
        return redirect(redirect_url)
    return render(request, 'ingame_api/submit_achievement.html', {'form': form})
