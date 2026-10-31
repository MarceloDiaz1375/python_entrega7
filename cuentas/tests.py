from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse


class PasswordChangeViewTests(TestCase):
    def test_password_change_page_renders_for_authenticated_user(self):
        user = User.objects.create_user(username="tester")
        self.client.force_login(user)

        response = self.client.get(reverse("password_change"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registro/password_change.html")
