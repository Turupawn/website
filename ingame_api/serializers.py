from rest_framework import serializers
from ingame_api import models

from games.models import Game
from games.serializers import GameSerializer

class StatSerializer(serializers.ModelSerializer):
    game = GameSerializer(many=False)

    class Meta(object):
        model = models.Stat
        fields = ('game', 'type','name','increment_only',
                  'max_change','min_change','max_value',
                  'window', 'default_value', 'aggregated')

class UserStatSerializer(serializers.ModelSerializer):
    stat = StatSerializer(many=False)

    class Meta(object):
        model = models.Achievement
        fields = ('value','user')

class AchievementSerializer(serializers.ModelSerializer):
    game = GameSerializer(many=False)
    stat = StatSerializer(many=False)

    class Meta(object):
        model = models.Achievement
        fields = ('game','name','description','achieved_icon','unachieved_icon','stat')

class UserAchievementSerializer(serializers.ModelSerializer):
    achievement = AchievementSerializer(many=False)

    class Meta(object):
        model = models.Achievement
        fields = ('competed','user')
