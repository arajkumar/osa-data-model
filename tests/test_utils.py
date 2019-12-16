#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test the common utilities."""
import json
import logging

from utils import decode_json


def test_decode_and_parse_json(caplog):
    assert decode_json(json.dumps({"somekey": "someval", "someotherkey": True,})) != {}
    caplog.set_level(logging.CRITICAL)
    assert decode_json("") == {}
