#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Load the data and pass on for graph creation, also contains our entrypoint."""
import argparse
import sys
import os
from graph_create.preprocess_create_schema import create_nodes


def prep_data(mul_fact):
    """Use the multiplying factor and sample data to create appropriate nodes."""
    for i in range(0, 10 ** mul_fact):
        create_nodes(i)


def main():
    """Driver program for data preparation."""
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
    if args.order_magnitude > 6 or args.order_magnitude < 1:
        sys.stderr.write(
            "Order of magnitude of data should be a number between 1 and 6 that "
            "will become a power of 10."
        )
        sys.exit(-1)
    prep_data(args.order_magnitude)


if __name__ == "__main__":
    main()
