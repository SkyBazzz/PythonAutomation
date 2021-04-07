import pytest


@pytest.mark.smoke
def test_passed(create_guys):
    alex1, alex2 = create_guys
    assert id(alex1) == id(alex2), "Singleton failed, variables contain different instances."
