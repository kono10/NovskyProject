from django.test import TestCase
from visuals.models import Visual, VizResource, Tag, VizType
from django.urls import reverse
from datetime import datetime as dt
import json


class TestViewRenders(TestCase):
    @classmethod
    def setUpTestData(cls):
        viz_body = """{"config": 
                {"view": 
                    {"continuousWidth": 400, "continuousHeight": 300}, 
                "axis": {"gridColor": "grey", "gridDash": [6, 4]}, 
                "axisBottom": {"labelColor": "#c83803", "labelFontSize": 15, "titleColor": "#c83803", "titleFontSize": 17}, 
                "axisLeft": {"labelColor": "#c83803", "labelFontSize": 17, "titleColor": "#c83803", "titleFontSize": 20}, 
                "background": "#0B162A", 
                "legend": {"cornerRadius": 10, "fillColor": "#0B162A", "labelColor": "#c83803", "labelFontSize": 17, "padding": 10, "strokeColor": "gray", "titleColor": "#c83803", "titleFontSize": 17},
                "title": {"color": "#c83803", "fontSize": 17}}, "hconcat": [{"data": {"name": "data-f4d146561bba45e94a9c9029c2251e67"}}]}"""
        viz_body_plotly = """{"data":[{"cells":{"align":["left","center"],"fill":{"color":"#0B162A"},"font":{"color":"white"}}}]}"""
        vt = VizType(name="Altair")
        vt.save()
        vtp = VizType(name="Plotly")
        vtp.save()
        t = Tag(name="Python")
        t.save()
        vr = VizResource(name="Google", url="www.google.com")
        vt.save()
        viz = Visual.objects.create(
            name="testViz", viz_type=vt, body=viz_body, pub_date=dt.now(),
        )
        viz.save()
        vizp = Visual.objects.create(
            name="testVizPlotly", viz_type=vtp, body=viz_body_plotly, pub_date=dt.now(),
        )
        vizp.save()
        cls.viz = viz
        cls.viz_plotly = vizp

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

    def test_detail_styles(self):
        self.assertEqual(self.viz.background_color, "#0B162A")
        self.assertEqual(self.viz.font_color, "#c83803")

    def test_api_get(self):
        """
        Test that the api returns data we expect
        """
        response = self.client.get("/api/visuals/")
        self.assertEqual(response.status_code, 200)
        json_data = json.loads(response.content)
        self.assertEqual(json_data["results"][0]["name"], "testViz")
