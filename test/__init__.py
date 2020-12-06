from contextlib import contextmanager

import pytest
from flask import template_rendered

from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


@contextmanager
def captured_templates(app):
    recorded = []

    def record(sender, template, context, **kwags):
        recorded.append((template, context))

    template_rendered.connect(record, app)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)
