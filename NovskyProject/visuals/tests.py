from django.test import TestCase
from visuals.models import Visual, VizResource, Tag, VizType
from django.urls import reverse
from datetime import datetime as dt


class TestViewRenders(TestCase):
    @classmethod
    def setUpTestData(cls):
        VizType.objects.create(name="HTML")
        VizType.objects.create(name="Altair")
        Tag.objects.create(name="Python")
        Tag.objects.create(name="Chicago Bears")
        VizResource(name="Google", url="www.google.com")
        cls.viz = Visual.objects.create(
            name="testViz",
            viz_type=VizType(id=1),
            body="<h1> this is a viz </h1>",
            pub_date=dt.now(),
            viz_resources=VizResource(id=1),
        )

    def test_index_page_render(self):
        """
        Test the landing page that lists visual names
        """
        response = self.client.get(reverse("visuals:index"))
        self.assertEqual(response.status_code, 200)

    def test_detail_page_render(self):
        """
        Test the page that actually renders the visual
        """
        pass

    def test_api_get(self):
        """
        Test that the api returns data we expect
        """
