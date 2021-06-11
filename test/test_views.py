from flask import request

from test import client
from test import captured_templates
from app import app
from app.db_handeler import DB_Handler
from helper.utils import make_title_from_url


def test_index(client):
    """ Testcase for index page """
    response = client.get("/")
    assert b"YOGESHWARAN R" in response.data


def test_posts(client):
    """ Testcase for jinja to get all posts from db """
    with captured_templates(app) as templates:
        client.get("/posts")
        _, context = templates[0]
        assert context["posts"] == DB_Handler.TablePost.all_query()


def test_post(client):
    """ Testcase for jinja to get post data from db """
    test_pat = "Instantly-Host-any-non-binary-files-from-your-terminal"
    with captured_templates(app) as templates:
        client.get(f"post/{test_pat}")
        _, context = templates[0]
        assert context["post"] == DB_Handler.TablePost.query_by_title(make_title_from_url(test_pat))


def test_project(client):
    """ Testcase for jinja to get all Projects from db """
    response = client.get("/projects")
    assert b"github" in response.data


def test_potfolio(client):
    """ Testcase for jinja to get portfolio data from db"""
    with captured_templates(app) as templates:
        client.get("/")
        _, context = templates[0]
    assert context["text"] == DB_Handler.TablePortfolio.text()


def test_404_error(client):
    """ Testcase for error page """
    response = client.get("/somthing_not_in_path")
    assert b"404" in response.data


def test_404_error_for_invalid_post_id(client):
    """ Testcase for error page for invalid post id """
    response = client.get("post?id=1000d")
    assert b"400" in response.data
