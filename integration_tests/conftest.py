"""Shared fixtures for the generated integration tests."""

import os

import pytest

from aspose.cells.cloud import CellsCloudClient


@pytest.fixture(scope="session")
def client():
    """A session-scoped client authenticated against the Aspose.Cells Cloud API."""
    client_id = os.environ.get("CellsCloudClientId")
    client_secret = os.environ.get("CellsCloudClientSecret")
    if not client_id or not client_secret:
        pytest.skip(
            "Set CellsCloudClientId and CellsCloudClientSecret to run "
            "integration tests."
        )
    return CellsCloudClient(
        client_id,
        client_secret,
        os.environ.get("CellsCloudApiBaseUrl", "https://api.aspose.cloud"),
    )
