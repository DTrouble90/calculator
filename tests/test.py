import pytest

from app.calc import Calculator

class TestCalc:
    def setup(selfself):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self, 1, 1) == 2

    def test_adding_unsuccess(self):
        assert self.calc.adding(self, 1, 1) == 3

    def test_substraction_success(self):
        assert self.calc.substraction(self, 2, 1) == 1

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(1, 0)

    def teardown(self):
        print("Выполнение метода Teardown")
