from django.test import TestCase
from django.urls import reverse
import os


class TestViewRenders(TestCase):
    def test_page_render(self):
        """
        Make sure a page renders without error
        """
        response = self.client.get(reverse("myapp:index"))
        self.assertEqual(response.status_code, 200)
