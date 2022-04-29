from django.test import TestCase, Client
from django.urls import reverse


class ViewTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_index_view(self) -> None:
        """ Test if index view returns HTTP 200 response """
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_api_view(self) -> None:
        """ Test if api_root view returns HTTP 200 response """
        url = reverse('api_root')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
