import pytest
import logging
from helpers.logger import setup_logger

@pytest.fixture(scope="session")
def logger():
    return setup_logger("TestLogger", level=logging.INFO)
