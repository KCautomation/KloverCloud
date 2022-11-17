import pytest


# @pytest.fixture()
# def tc_setup():
#     print("launch1")
#     print("login")
#
#     yield
#     print("logout")
#     print("close browser")

@pytest.fixture()
def setUp():
    print("before you can")

    yield
    print("after run all test")


@pytest.Test()
def test_add(setUp):
    print("added")
