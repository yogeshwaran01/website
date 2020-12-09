from contextlib import contextmanager

import pytest
from flask import template_rendered

from app import app


@pytest.fixture
def client():
    """ Init Pytest """
    with app.test_client() as client:
        yield client


@contextmanager
def captured_templates(app):
    """ Function return the data from jinja templates """
    recorded = []

    def record(sender, template, context, **kwags):
        recorded.append((template, context))

    template_rendered.connect(record, app)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)
