"""Strangeworks SDK."""

import importlib.metadata

from .client import Client
from .config import config

__version__ = importlib.metadata.version("strangeworks")

cfg = config.Config()
client = Client(cfg=cfg)  # instantiate a client on import by default

# strangeworks.(public method)
authenticate = client.authenticate
workspace_info = client.workspace_info
resources = client.resources
execute = client.execute
jobs = client.jobs
