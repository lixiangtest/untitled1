import pytest


# 数据共享文件，可以直接被其他方法调用
@pytest.fixture()
def login():
    print(u"登录成功")
