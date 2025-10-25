import unittest
import main


class TestLambda(unittest.TestCase):
    def test_true(self):
        self.check(main.TRUE, True)

    def test_false(self):
        self.check(main.FALSE, False)

    def test_and(self):
        self.check(main.AND(main.TRUE)(main.TRUE), True)
        self.check(main.AND(main.TRUE)(main.TRUE), True)
        self.check(main.AND(main.TRUE)(main.TRUE), True)
        self.check(main.AND(main.TRUE)(main.TRUE), True)

    def check(self, inp, exp):
        out = main.eval_bool(inp)
        self.assertEqual(exp, out)


if __name__ == "__main__":
    unittest.main()
