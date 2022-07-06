#tests/test_app.py

import unittest
import os
os.environ['TESTING'] = 'true'

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>MLH Fellow</title>" in html
        assert '<img src="./static/img/logo.svg" />' in html


    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        # assert len(json["timeline_posts"]) == 0

        # check post request
        post_response = self.client.post('/api/timeline_post', data=dict(name="dummy name", email="dummy@email.com", content="dummy content"))
        assert post_response.status_code == 200
        assert post_response.is_json
        post_json = post_response.get_json()
        assert post_json['content'] == "dummy content"
        # assert post_json['id'] == 1;
        assert post_json['name'] == 'dummy name'

        new_response = self.client.get("/api/timeline_post")
        assert new_response.status_code == 200
        assert new_response.is_json
        new_json = new_response.get_json()
        assert len(new_json["timeline_posts"]) > 0

        timeline_response = self.client.get("/timeline")
        assert timeline_response.status_code == 200
        html = timeline_response.get_data(as_text=True)
        assert '<form id="form">' in html

    def test_malformed_timeline_post(self):
        # POST request missing name
        response = self.client.post("/api/timeline_post", data=
        {"email": "john@example.com", "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid name" in html

        # POST request with empty content
        response = self.client.post("/api/timeline_post", data=
        {"name": "John Doe", "email": "john@example.com", "content": ""})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid content" in html

        # POST request with malformed email
        response = self.client.post("/api/timeline_post", data=
        {"name": "John Doe", "email": "not-an-email", "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html
