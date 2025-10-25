TRUE = lambda x: lambda y: x
FALSE = lambda x: lambda y: y
AND = lambda x: lambda y: x(y)(FALSE)
NOT = lambda x: x(FALSE)(TRUE)
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

POWER = lambda m: lambda n: n(m)
# understood it the following way:
# POWER_3 = lambda f: lambda x: THREE(THREE(THREE(f)))(x)
# POWER_3_2 = lambda f: lambda x: THREE(THREE)(f)(x)
# compose three with three to get 3^3

SUCC = lambda n: lambda f: lambda x: f(n(f)(x))
# key piece of insight is we supply a function that short circuits and forcibly returns x once

# fmt: off
PRED = lambda n: lambda f: lambda x: n(\
    lambda g: lambda h: h(g(f))\
)(lambda _: x)(lambda i:i)
# fmt: on

SUB = lambda m: lambda n: n(PRED)(m)

IS_ZERO = lambda n: n(lambda _: FALSE)(TRUE)


def eval_bool(x):
    return x(True)(False)


def eval_num(x):
    return x(lambda x: x + 1)(0)
