#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test the common utilities."""
import json
import logging

from utils import decode_and_parse_json


def test_decode_and_parse_json(caplog):
    assert (
        decode_and_parse_json(json.dumps({"somekey": "someval", "someotherkey": True,}))
        != {}
    )
    assert decode_and_parse_json("") == {}
    caplog.set_level(logging.CRITICAL)
    captured = caplog.get_records("call")
    assert "Unable to process JSON , got error" in captured[0].getMessage()
