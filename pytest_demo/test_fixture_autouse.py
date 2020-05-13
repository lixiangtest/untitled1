import pytest


# autouse可以把open()方法自动使用到每个方法中
@pytest.fixture(scope="module", autouse=True)
def open():
    print("open start")
    yield
    print("open over")
    raise NameError


def test_search01():
    print("search 01")


def test_search02():
    print("search 02")


def test_search03():
    print("search 03")


if __name__ == "__main__":
    pytest.main()
