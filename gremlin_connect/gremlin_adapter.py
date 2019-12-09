"""Contains benchmarks for the graph database for the Go-CVE use case."""
import requests
import json
from json import JSONDecodeError
from urllib.parse import urlparse
import logging

logging.basicConfig()
logger = logging.getLogger(__name__)

GREMLIN_DEFAULT_PORT = 8182
GREMLIN_DEFAULT_HOST = "localhost"


class GremlinAdapter:
    """Interactions with the Gremlin server."""

    def __init__(self, gremlin_host=GREMLIN_DEFAULT_HOST):
        """Initialize an object of the adapter class."""
        super().__init__()
        self._gremlin_host = gremlin_host
        self._gremlin_port = GREMLIN_DEFAULT_PORT

    @property
    def gremlin_host(self):
        """Define the gremlin host."""
        return self._gremlin_host

    @property
    def gremlin_port(self):
        """Specify the gremlin port information."""
        return self._gremlin_port

    @gremlin_host.setter
    def gremlin_host(self, gremlin_host):
        """Set the gremlin host server."""
        self._gremlin_host = gremlin_host

    @gremlin_port.setter
    def gremlin_port(self, gremlin_port):
        """Set the port for the gremlin server."""
        self._gremlin_port = gremlin_port

    @property
    def gremlin_url(self):
        """Get the url of the gremlin server."""
        return "http://{}:{}/".format(self.gremlin_host, self.gremlin_port)

    @gremlin_url.setter
    def gremlin_url(self, gremlin_url):
        """Set the complete connection url for the gremlin server."""
        gremlin_url = gremlin_url.replace("http://", "")
        host, port = gremlin_url.split(":")
        self._gremlin_host = host
        self._gremlin_port = port

    def test_connection(self):
        """Test connection to gremlin server."""
        response = requests.get(self.gremlin_url)
        # Everything except "not found" is acceptable.
        return response.status_code != 404

    def execute_query(self, query):
        """Execute a query on the Gremlin server."""
        response = requests.get(self.gremlin_url, params={"gremlin": query})
        try:
            return json.loads(response.json())
        except JSONDecodeError:
            return json.loads({})
