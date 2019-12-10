#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List, Dict
import os
import json
import argparse


def main():
    """The main driver program for data preparation."""
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument(
        "--order-magnitude",
        help="The order of magnitude (power of ten) of number of nodes in graph. "
        "Accepted values: [1, 6]",
        type=int,
        default=1,
        required=True,
    )
    args = argument_parser.parse_args()
    print(args.order_magnitude)


if __name__ == "__main__":
    main()
