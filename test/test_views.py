from flask import request

from test import client
from test import captured_templates
from app import app
from app.db_handeler import DB_Handler
from helper.github_repos import github_repo


def test_index(client):
    response = client.get("/")
    assert b"YOGESHWARAN R" in response.data


def test_posts(client):
    with captured_templates(app) as templates:
        response = client.get("/posts")
        _, context = templates[0]
        assert context["posts"] == DB_Handler.TablePost.all_query()


def test_post(client):
    with captured_templates(app) as templates:
        response = client.get("post?id=1")
        _, context = templates[0]
        assert request.args["id"] == "1"
        assert context["post"] == DB_Handler.TablePost.query_by_id(1)


def test_contact(client):
    with captured_templates(app) as templates:
        response = client.get("/projects")
        _, context = templates[0]
    assert context["repos"] == github_repo()
