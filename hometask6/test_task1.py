import pytest
import logging
import time

logger = logging.getLogger("test_task1")





def setup_module():
    logger.info("Started module")


def test_passed():
    time.sleep(2)
    assert True


@pytest.mark.usefixtures('request_fixture')
def test_failed():
    time.sleep(2)
    assert False


@pytest.fixture()
def before_method():
    logger.debug("Before method")


@pytest.fixture()
def request_fixture(request):
    logger.debug(f"Node name is {request.node.name}")
