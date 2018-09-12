from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
# from autofixture import AutoFixture

class HomeViewTestCase(TestCase):
    def setUp(self):
        self.username = 'myuser'
        self.password = 'valid_password1'
        self.client = Client()
        self.url = reverse('Visa:visacountry')
        User.objects.create_user(username=self.username, email='email@test.com', is_active=True, password=self.password)

    def test_home_view_redirects_authenticated_user_to_list(self):
        self.client.login(username = self.username, password = self.password)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
