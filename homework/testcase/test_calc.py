import math
from homework.demototest.calc import Calc
import pytest
import yaml
import os

Npath = os.path.abspath(os.path.join(os.getcwd(), ".."))
calc = Calc()


class TestCal:

    @pytest.mark.parametrize("param1, param2, expect", yaml.safe_load(open(Npath + "\configure\\addyaml")))
    def test_add(self, param1, param2, expect):
        result = calc.add(param1, param2)
        if isinstance(param1, (int, float)) and isinstance(param2, (int, float)) is not True:
            raise TypeError("传入的参数不是int类型")
        else:
            assert math.isclose(result, expect)

    @pytest.mark.parametrize("param1, param2, expect", yaml.safe_load(open(Npath + "\configure\subyaml")))
    def test_sub(self, param1, param2, expect):
        result = calc.sub(param1, param2)
        assert math.isclose(result, expect)

    @pytest.mark.parametrize("param1, param2, expect", yaml.safe_load(open(Npath + "\configure\mulyaml")))
    def test_mul(self, param1, param2, expect):
        result = calc.mul(param1, param2)
        assert math.isclose(result, expect)

    @pytest.mark.parametrize("param1, param2, expect", yaml.safe_load(open(Npath + "\configure\divyaml")))
    def test_div(self, param1, param2, expect):
        result = calc.div(param1, param2)
        assert math.isclose(result, expect)


if __name__ == '__main__':
    pytest.main()
