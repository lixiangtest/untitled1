from homework.demototest.calc import Calc
from pytest import approx


class TestCal:
    calc = Calc()

    def test_add_001(self):
        result = self.calc.add(1, 2)
        assert 3 == result

    def test_add_002(self):
        result = self.calc.add(0.1, 0.2)
        assert approx(0.3) == result
