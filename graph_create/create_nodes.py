#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Create the nodes in the graph."""
from gremlin_connect.gremlin_adapter import GremlinAdapter
from typing import List, Dict


class CreateNodesInGraph:
    """Create all the nodes in the graph."""

    gremlin_adapter = GremlinAdapter()

    @classmethod
    def create_probable_vuln_node(cls, prob_cve_id):
        """Create a new probable vulnerability node."""
        query = cls.label_builder("probable_vulnerability") + cls.property_builder(
            vertex_label="probable_vulnerability", probable_cve_id=prob_cve_id
        )
        return cls.gremlin_adapter.execute_query(query)

    @classmethod
    def create_dependency_node(cls):
        """Create a new dependency node."""
        pass

    @classmethod
    def create_reported_cve_node(cls):
        """Create a new reported CVE node."""
        pass

    @classmethod
    def create_feedback_node(cls):
        """Create a new feedback node."""
        pass

    @classmethod
    def create_security_event_node(cls):
        """Create a new security event node."""
        pass

    @classmethod
    def create_dependency_version_node(cls, version, dep_name):
        """Create a new dependency version node."""
        query = cls.label_builder("dependency_version") + cls.property_builder(
            version=version, dependency_name=dep_name, vertex_label="dependency_version"
        )
        return cls.gremlin_adapter.execute_query(query)

    @classmethod
    def create_ecosystem_node(cls, ecosystem_name):
        """Create a new ecosystem node."""
        query = cls.label_builder("ecosystem") + cls.property_builder(
            ecosystem=ecosystem_name, vertex_label="ecosystem"
        )
        return cls.gremlin_adapter.execute_query(query)

    @staticmethod
    def label_builder(label_name: str) -> str:
        """
        Generate the label name for a node.

        Args:
            label_name: The label name to assign to this node.

        Returns:
            Part of the gremlin query g.V(label_name).

        """
        return "g.V('{}')".format(label_name)

    @staticmethod
    def property_builder(**kwargs) -> str:
        """Use a variable size list of properties to get back a .property() querystring."""
        prop_str = ""
        for p, val in kwargs.items():
            prop_str = "{}.property('{}', '{}')".format(prop_str, str(p), str(val))
        return prop_str
