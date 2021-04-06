import logging

logger = logging.getLogger("conftest")


def pytest_sessionstart(session):
    print("Even before session")
    logger.debug(session)


def pytest_sessionfinish(session):
    print("After session ends")
    logger.debug(session)
