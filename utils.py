#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains the utility functions used accross the project."""
import json
from typing import Dict
import daiquiri


def decode_json(json_str: str) -> Dict:
    """Decode the supplied JSON string and return a Dict, with full error handling."""
    try:
        decoded = json.loads(json_str)
    except json.decoder.JSONDecodeError as e:
        daiquiri.logging.error(
            "Unable to process JSON {}, got error {}".format(json_str, e)
        )
        decoded = {}
    return decoded
