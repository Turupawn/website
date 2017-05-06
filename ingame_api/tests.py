from django.test import TestCase
from django.db import models
from django.contrib.auth import get_user_model
from ingame_api import models

class TestAchievement(TestCase):
    def test_instanciation(self):
        achievement = models.Achievement()
        achievement.name = 'Win the game'
        achievement.description = 'Just win'
        self.assertEqual(achievement.name, 'Win the game')
        self.assertEqual(achievement.description, 'Just win')

    def test_foreign_keys(self):
        game = models.Game()
        game.name = 'Warsov'
        stat = models.Stat()
        stat.name = 'Win count'
        achievement = models.Achievement()
        achievement.game = game
        achievement.stat = stat
        self.assertEqual(achievement.game.name, 'Warsov')
        self.assertEqual(achievement.stat.name, 'Win count')

class TestStat(TestCase):
    def test_instanciation(self):
        stat = models.Stat()
        stat.name = 'Best score'
        stat.increment_only = True
        stat.max_change = 0
        stat.min_change = 0
        stat.max_value = 100
        stat.window = 0
        stat.default_value = 0
        stat.aggregated = 0
        self.assertEqual(stat.name, 'Best score')
        self.assertEqual(stat.increment_only, True)
        self.assertEqual(stat.max_change, 0)
        self.assertEqual(stat.min_change, 0)
        self.assertEqual(stat.max_value, 100)
        self.assertEqual(stat.window, 0)
        self.assertEqual(stat.default_value, 0)
        self.assertEqual(stat.aggregated, 0)

    def test_game_foreign_key(self):
        game = models.Game()
        game.name = 'OpenRA'
        stat = models.Stat()
        stat.game = game
        self.assertEqual(stat.game.name, 'OpenRA')

class TestUserStat(TestCase):
    def test_instanciation(self):
        user_stat = models.UserStat()
        user_stat.value = 1337
        self.assertEqual(user_stat.value, 1337)

    def test_foreign_keys(self):
        User = get_user_model()
        user = User()
        user.username = 'test'
        stat = models.Stat()
        stat.name = 'Win the game'
        user_stat = models.UserStat()
        user_stat.user = user
        user_stat.stat = stat
        self.assertEqual(user_stat.user.username, 'test')
        self.assertEqual(user_stat.stat.name, 'Win the game')
