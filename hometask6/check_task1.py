import pytest
import logging
import time
from hometask4.task3 import Engineer, Manager

logger = logging.getLogger("test_task1")


def setup_module():
    logger.info("Started module")


@pytest.mark.smoke
def test_passed(before_method):
    # add some employees
    alex = Engineer('Alex', 55)
    alex.join_company(before_method)
    alex.do_work()

    jane = Manager('Jane', 30)
    jane.join_company(before_method)
    # Jane works pretty hard. She writes lots of reports
    jane.do_work()
    jane.do_work()
    assert before_method.balance == 966


@pytest.mark.xfail
def test_failed():
    assert False
