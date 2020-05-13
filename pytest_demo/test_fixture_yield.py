import pytest


# yield相当于setup teardown，第一次执行调用yield前面的内容，最后一次执行调用yield后面的内容
@pytest.fixture(scope="module")
def open():
    print("open start")
    yield
    print("open over")
    raise NameError


def test_search01(open):
    print("search 01")


def test_search02(open):
    print("search 02")


def test_search03(open):
    print("search 03")


if __name__ == "__main__":
    pytest.main()
