import pytest

from hometask7 import log
from hometask4.task3 import Alex


@pytest.fixture()
def create_guys():
    log.debug("Setup guys")
    alex1 = Alex()
    alex2 = Alex()
    yield alex1, alex2
