T = lambda x: lambda y: x
F = lambda x: lambda y: y
AND = lambda x: lambda y: x(y, F)
OR = lambda x: lambda y: x(T, y)
I = lambda x: x

ZERO = lambda f: lambda x: x
ONE = lambda f: lambda x: f(x)
PLUS = lambda m: lambda n: lambda f: lambda x: m(f)(n(f)(x))
SUCC = lambda n: lambda f: lambda x: f(n(f)(x))
# SUCC = lambda n: PLUS(ONE)(n)

# notice the n(f)(x). It's basically identity for numbers
I_NUM = lambda n: lambda f: lambda x: n(f)(x)

TWO = SUCC(ONE)
THREE = SUCC(TWO)
FOUR = SUCC(THREE)
FIVE = SUCC(FOUR)

TIMES = lambda m: lambda n: lambda f: lambda x: m(n(f))(x)
TEN = TIMES(TWO)(FIVE)
HUNDRED = TIMES(TEN)(TEN)


def eval_bool(x):
    print(x("true")("false"))


def eval_ident(x):
    print(x("identity"))


def eval_num(x):
    print(x(lambda x: x + 1)(0))


eval_num(HUNDRED)

# eval_bool(AND(T, T))
# eval_bool(AND(T, F))
# eval_bool(AND(F, T))
# eval_bool(AND(F, F))

# eval_bool(OR(T, T))
# eval_bool(OR(T, F))
# eval_bool(OR(F, T))
# eval_bool(OR(F, F))
