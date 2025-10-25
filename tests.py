import unittest
import main


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

    def test_or(self):
        self.check(main.OR(main.TRUE)(main.TRUE), True)
        self.check(main.OR(main.TRUE)(main.FALSE), True)
        self.check(main.OR(main.FALSE)(main.TRUE), True)
        self.check(main.OR(main.FALSE)(main.FALSE), False)

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

    def check(self, inp, exp):
        out = main.eval_num(inp)
        self.assertEqual(exp, out)


if __name__ == "__main__":
    unittest.main()
