import pytest


@pytest.mark.singleton
def test_singleton(create_guys):
    alex1, alex2 = create_guys
    assert id(alex1) == id(alex2), "Singleton failed, variables contain different instances."
