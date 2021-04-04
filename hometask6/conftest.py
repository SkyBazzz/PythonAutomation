import pytest
import logging

logger = logging.getLogger("conftest")


@pytest.hookimpl(tryfirst=True)
def pytest_sessionstart(session):
    print("StartingXXX")
    logger.debug("hello")
