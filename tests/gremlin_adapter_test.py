"""Tests for the gremlin adapter."""
import unittest
from gremlin_connect.gremlin_adapter import GremlinAdapter
import requests
import pytest
import json
from conftest import gremlin_get


def test_execute_query(monkeypatch):
    """Test the query execution method."""
    monkeypatch.setattr(requests, "get", gremlin_get)
    assert GremlinAdapter().execute_query("g.V().count()") == {
        "executed": "g.V().count()"
    }
