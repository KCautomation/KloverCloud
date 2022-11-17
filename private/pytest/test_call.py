import pytest


@pytest.fixture()
def test_add(setUp):
    print("added")


def test_remove(setUp):
    print("removed")


def test_method(setUp):
    print("A is running to test")


def test_math(setUp):
    print("B is running to test")
