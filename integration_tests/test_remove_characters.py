"""Integration tests for RemoveCharacters (generated from TestingData)."""

import os

import pytest

from aspose.cells.cloud import CellsCloudClient
from aspose.cells.cloud.request import RemoveCharactersByPositionRequest
from aspose.cells.cloud.request import RemoveCharactersRequest
from aspose.cells.cloud.request import RemoveDuplicateSubstringsRequest


def test_remove_characters(client):
    """Test for update word case local spreadsheet file.."""
    request = RemoveCharactersRequest(
        worksheet="Text",
        remove_text_method="RemoveCharacterSets",
        character_sets="NonPrintingCharacters",
        spreadsheet="testdata/BookText.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_remove_duplicate_substrings(client):
    """Test for update word case local spreadsheet file.."""
    request = RemoveDuplicateSubstringsRequest(
        worksheet="Text",
        delimiters="Space",
        spreadsheet="testdata/BookText.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_remove_characters_with_first_n_characters(client):
    """Test for update word case local spreadsheet file.."""
    request = RemoveCharactersByPositionRequest(
        worksheet="Text",
        the_first_n_characters=5,
        the_last_n_characters=3,
        spreadsheet="testdata/BookText.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_remove_characters_with_all_characters_before_text(client):
    """Test for update word case local spreadsheet file.."""
    request = RemoveCharactersByPositionRequest(
        worksheet="Text",
        the_first_n_characters=0,
        the_last_n_characters=0,
        all_characters_before_text="Designed",
        all_characters_after_text="distance",
        spreadsheet="testdata/BookText.xlsx",
    )

    response = client.do(request)
    assert response is not None


def test_remove_characters_by_position(client):
    """Test for update word case local spreadsheet file.."""
    request = RemoveCharactersByPositionRequest(
        the_first_n_characters=5,
        the_last_n_characters=3,
        spreadsheet="testdata/BookText.xlsx",
    )

    response = client.do(request)
    assert response is not None
