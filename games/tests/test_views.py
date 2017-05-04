import json
from django.test import TestCase
from django.urls import reverse
from django.conf import settings
from . import factories


class TestInstallerViews(TestCase):
    def setUp(self):
        self.game = factories.GameFactory(name='doom', slug='doom')
        self.user = factories.UserFactory()

    def test_anonymous_user_cant_create_installer(self):
        factories.GameFactory()
        installer_url = reverse("new_installer", kwargs={'slug': 'doom'})
        response = self.client.get(installer_url, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(settings.LOGIN_URL + '?next=' + installer_url,
                         response.redirect_chain[1][0])

    def test_logged_in_user_can_create_installer(self):
        self.client.login(username=self.user.username, password="password")
        installer_url = reverse("new_installer", kwargs={'slug': 'doom'})
        response = self.client.get(installer_url)
        self.assertEqual(response.status_code, 200)

    def test_can_redirect_to_game_page_from_installer_slug(self):
        installer = factories.InstallerFactory(game=self.game)

        game_for_installer_url = reverse("game_for_installer",
                                         kwargs={'slug': installer.slug})
        response = self.client.get(game_for_installer_url)
        self.assertRedirects(
            response, reverse('game_detail', kwargs={'slug': self.game.slug})
        )

    def test_can_access_installer_feed(self):
        response = self.client.get('/games/installer/feed/')
        self.assertEqual(response.status_code, 200)


class TestGameViews(TestCase):
    def test_can_get_game_list(self):
        response = self.client.get(reverse('game_list'))
        self.assertEqual(response.status_code, 200)
