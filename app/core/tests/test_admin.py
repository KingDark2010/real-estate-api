from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email="admin@testing.com",
            password="password123"
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email="test@testing.com",
            password="password123",
            name="Name Testing"
        )

    def test_user_listed(self):
        """test user if listed in user page"""
        url = reverse('admin:core_user_changelist')
        responses = self.client.get(url)

        self.assertContains(responses, self.user.name)
        self.assertContains(responses, self.user.email)

    def test_user_change_page(self):
        """test user editing page is working"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """test that user create page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
