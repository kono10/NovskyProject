from django.test import TestCase
from visuals.models import Visual, VizResource, Tag, VizType
from visuals.views import IndexView
from django.urls import reverse
from datetime import datetime as dt
import json
import logging


class TestViewRenders(TestCase):
    fixtures = ["db.json"]

    @classmethod
    def setUpTestData(cls):
        cls.all_viz = Visual.objects.order_by("-pub_date")
        logging.warning(f"Loading {len(cls.all_viz)} records from test db")
        logging.warning(f"First Record ==> {cls.all_viz[0]} ")
        cls.viz_altair = Visual.objects.get(pk=1)
        cls.viz_plotly = Visual.objects.get(pk=19)

    def test_index_page_render(self):
        """
        Test the landing page that lists visual names
        """
        response = self.client.get(reverse("visuals:index"))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context["latest_visual_list"],
            self.all_viz[: IndexView.paginate_by],
        )

    def test_detail_page_render(self):
        """
        Test the page that actually renders the visual
        """
        response = self.client.get(reverse("visuals:detail", args={self.viz_altair.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["visual"].name, self.viz_altair.name)

    def test_detail_styles(self):

        self.assertEqual(self.viz_altair.background_color, "#0B162A")
        self.assertEqual(self.viz_altair.font_color, "#C83803")

        self.assertEqual(self.viz_plotly.background_color, "#0B162A")
        self.assertEqual(self.viz_plotly.font_color, "white")

    def test_api_get(self):
        """
        Test that the api returns data we expect
        """
        response = self.client.get("/api/visuals/")
        self.assertEqual(response.status_code, 200)
        json_data = json.loads(response.content)
        self.assertEqual(
            json_data["results"][0]["name"], "Chicago Bears Strength of Schedule"
        )
