__author__ = "Darsh Shukla"

import os
import pytest
from configparser import ConfigParser
from zype import Zype


@pytest.fixture
def api_key():
    config = ConfigParser()
    config.read(
        os.path.join(os.path.abspath(os.path.dirname(__file__)), "", "config.ini")
    )
    _api_key = config.get("KEYS", "APIKey")
    return _api_key


def test_list_videos(api_key):
    client = Zype(api_key=api_key)
    videos = client.list_videos().get()
    assert videos().data is not None

def test_list_streams_hours(api_key):
    client = Zype(api_key=api_key, api_root="https://analytics.zype.com")
    stream_hours = client.list_stream_hours().get()
    assert stream_hours().data is not None