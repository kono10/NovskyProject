from django.test import TestCase
from visuals.models import Visual, VizResource, Tag, VizType
from django.urls import reverse
from datetime import datetime as dt
import json


class TestViewRenders(TestCase):
    @classmethod
    def setUpTestData(cls):
        vt = VizType(name="HTML")
        vt.save()
        t = Tag(name="Python")
        t.save()
        vr = VizResource(name="Google", url="www.google.com")
        vt.save()
        viz = Visual.objects.create(
            name="testViz",
            viz_type=vt,
            body="<h1> this is a viz </h1>",
            pub_date=dt.now(),
        )
        viz.save()
        cls.viz = viz

    def test_index_page_render(self):
        """
        Test the landing page that lists visual names
        """
        response = self.client.get(reverse("visuals:index"))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context["latest_visual_list"], [self.viz])

    def test_detail_page_render(self):
        """
        Test the page that actually renders the visual
        """
        response = self.client.get(reverse("visuals:detail", args={self.viz.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["visual"].name, "testViz")

    def test_api_get(self):
        """
        Test that the api returns data we expect
        """
        response = self.client.get("/api/visuals/")
        self.assertEqual(response.status_code, 200)
        json_data = json.loads(response.content)
        self.assertEqual(json_data["results"][0]["name"], "testViz")
