import pytest

from hometask6 import log
from hometask4.task3 import Company


@pytest.fixture()
def before_method():
    log.debug("Setup company")
    fruits_company = Company('Fruits', address='Ocean street, 1')
    yield fruits_company


def pytest_sessionstart(session):
    log.debug(f"Even before session - {session}")


def pytest_sessionfinish(session):
    log.debug(f"After session ends - {session}")


def pytest_html_report_title(report):
    report.title = "My very own title!"


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(report, "duration_formatter", "%H:%M:%S.%f")
