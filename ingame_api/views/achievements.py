from __future__ import absolute_import

import logging

from django.conf import settings
from rest_framework import filters, generics, permissions
from rest_framework.response import Response
from django.http import JsonResponse
from django.urls import reverse

from ingame_api.forms import (AchievementForm)
from django.shortcuts import get_object_or_404, redirect, render

LOGGER = logging.getLogger(__name__)

#from ingame_api import models, serializers

class UnlockAchievementView(generics.GenericAPIView):

    def get(self, request, achievement_id):
        return JsonResponse({'message':'achievement was unlocked'})

class GetAchievementsView(generics.GenericAPIView):

    def get(self, request, username, achievement_id):
        return JsonResponse({
                              "achivements":
                              [
                                {
                                  'completed': True,
                                  'achievement':
                                  {
                                    'id': 101, 'name': "Win the game", 'Description': "Just win",
                                    'achieved_icon': "game/321/win.png", 'unachieved_icon': "game/321/win.png",
                                    'progress_stat':None
                                  }
                                },
                                {
                                  'completed': False,
                                  'achievement':
                                  {
                                    'id': 102, 'name': "Win 100 times", 'Description': "Just over and over again",
                                    'achieved_icon': "game/321/100wins.png", 'unachieved_icon': "game/321/100wins.png",
                                    'progress_stat':
                                    {
                                      'stat_id': 321, 'stat_name': "wins",'min_value': 0, 'max_value': 100, 'current_value': 56
                                    }
                                  }
                                }
                              ]
                            })

def submit_achievement(request):
    form = AchievementForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        achievement = form.save()

        redirect_url = request.build_absolute_uri(reverse("api_achievement_add"))

        # Enforce https
        if not settings.DEBUG:
            redirect_url = redirect_url.replace('http:', 'https:')

        LOGGER.info('Achievement submitted, redirecting to %s', redirect_url)
        return redirect(redirect_url)
    return render(request, 'achievements/submit.html', {'form': form})
