import unittest
import main
import sys


class TestBoolLambda(unittest.TestCase):
    def test_true(self):
        self.check(main.TRUE, True)

    def test_false(self):
        self.check(main.FALSE, False)

    def test_and(self):
        self.check(main.AND(main.TRUE)(main.TRUE), True)
        self.check(main.AND(main.TRUE)(main.FALSE), False)
        self.check(main.AND(main.FALSE)(main.TRUE), False)
        self.check(main.AND(main.FALSE)(main.FALSE), False)

    def test_not(self):
        self.check(main.NOT(main.TRUE), False)
        self.check(main.NOT(main.FALSE), True)

    def test_or(self):
        self.check(main.OR(main.TRUE)(main.TRUE), True)
        self.check(main.OR(main.TRUE)(main.FALSE), True)
        self.check(main.OR(main.FALSE)(main.TRUE), True)
        self.check(main.OR(main.FALSE)(main.FALSE), False)

    def test_is_zero(self):
        self.check(main.IS_ZERO(main.ZERO), True)
        self.check(main.IS_ZERO(main.ONE), False)
        self.check(main.IS_ZERO(main.TWO), False)
        self.check(main.IS_ZERO(main.THREE), False)

    def check(self, inp, exp):
        out = main.eval_bool(inp)
        self.assertEqual(exp, out)


class TestNumLambda(unittest.TestCase):
    def test_zero(self):
        self.check(main.ZERO, 0)

    def test_one(self):
        self.check(main.ONE, 1)

    def test_succ(self):
        self.check(main.SUCC(main.ONE), 2)
        self.check(main.SUCC(main.SUCC(main.ONE)), 3)

    def test_numerals(self):
        self.check(main.TWO, 2)
        self.check(main.THREE, 3)
        self.check(main.FOUR, 4)
        self.check(main.FIVE, 5)

    def test_plus(self):
        self.check(main.PLUS(main.TWO)(main.ONE), 3)
        self.check(main.PLUS(main.TWO)(main.TWO), 4)

    def test_times(self):
        self.check(main.TIMES(main.TWO)(main.ONE), 2)
        self.check(main.TIMES(main.TWO)(main.TWO), 4)
        self.check(main.TIMES(main.TWO)(main.THREE), 6)
        self.check(main.TIMES(main.TWO)(main.FOUR), 8)

    def test_power(self):
        self.check(main.POWER(main.TWO)(main.TWO), 4)
        self.check(main.POWER(main.TWO)(main.THREE), 8)
        self.check(main.POWER(main.TWO)(main.FOUR), 16)

        self.check(main.POWER(main.FOUR)(main.TWO), 16)
        self.check(main.POWER(main.FOUR)(main.THREE), 64)

    def test_pred(self):
        self.check(main.PRED(main.ZERO), 0)
        self.check(main.PRED(main.ONE), 0)
        self.check(main.PRED(main.TWO), 1)
        self.check(main.PRED(main.THREE), 2)
        self.check(main.PRED(main.FOUR), 3)

    def test_sub(self):
        self.check(main.SUB(main.ONE)(main.TWO), 0)
        self.check(main.SUB(main.THREE)(main.TWO), 1)
        self.check(main.SUB(main.FOUR)(main.TWO), 2)

    def check(self, inp, exp):
        out = main.eval_num(inp)
        self.assertEqual(exp, out)


class TestLoop(unittest.TestCase):
    def test_loop(self):
        self.assertRaises(RecursionError, lambda: main.LOOP_FACTORY(None))

    def test_y(self):
        self.assertRaises(RecursionError, lambda: main.Y(None))

    def test_until_zero(self):
        self.check_bool(main.UNTIL_ZERO(main.ZERO), True)
        self.check_bool(main.UNTIL_ZERO(main.ONE), True)
        self.check_bool(main.UNTIL_ZERO(main.TWO), True)
        self.check_bool(main.UNTIL_ZERO(main.THREE), True)

    def check_bool(self, inp, exp):
        out = main.eval_bool(inp)
        self.assertEqual(exp, out)


if __name__ == "__main__":
    unittest.main()
