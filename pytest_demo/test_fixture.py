import pytest


def test_case1(login):
    print("need login")


def test_case2():
    print("not need login")


def test_case3(login):
    print("need login")


if __name__ == '__main__':
    pytest.main()
