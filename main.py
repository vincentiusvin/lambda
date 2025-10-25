TRUE = lambda x: lambda y: x
FALSE = lambda x: lambda y: y
AND = lambda x: lambda y: x(y)(FALSE)
OR = lambda x: lambda y: x(TRUE)(y)

ZERO = lambda f: lambda x: x
ONE = lambda f: lambda x: f(x)
PLUS = lambda m: lambda n: lambda f: lambda x: m(f)(n(f)(x))
SUCC = lambda n: lambda f: lambda x: f(n(f)(x))
# SUCC = lambda n: PLUS(ONE)(n)

# notice the n(f)(x). It's basically identity for numbers
# I_NUM = lambda n: lambda f: lambda x: n(f)(x)

TWO = SUCC(ONE)
THREE = SUCC(TWO)
FOUR = SUCC(THREE)
FIVE = SUCC(FOUR)

TIMES = lambda m: lambda n: lambda f: lambda x: m(n(f))(x)
TEN = TIMES(TWO)(FIVE)
HUNDRED = TIMES(TEN)(TEN)


def eval_bool(x):
    return x(True)(False)


def eval_num(x):
    return x(lambda x: x + 1)(0)
