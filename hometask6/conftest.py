import logging

import pytest

from hometask6.firm import Company

logger = logging.getLogger("conftest")


@pytest.fixture()
def before_method():
    logger.debug("Setup company")
    fruits_company = Company('Fruits', address='Ocean street, 1')
    yield fruits_company


def pytest_sessionstart(session):
    logger.debug(f"Even before session - {session}")


def pytest_sessionfinish(session):
    logger.debug(f"After session ends - {session}")


def pytest_html_report_title(report):
    report.title = "My very own title!"


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(report, "duration_formatter", "%H:%M:%S.%f")
