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


# key piece of insight is we supply a function that short circuits and forcibly returns x once
# fmt: off
PRED = lambda n: lambda f: lambda x: n(\
    lambda g: lambda h: h(g(f))\
)(lambda _: x)(lambda i:i)
# fmt: on

SUB = lambda m: lambda n: n(PRED)(m)

IS_ZERO = lambda n: n(lambda _: FALSE)(TRUE)

# because we want to run this on demand, wrap it in another lambda
# a pure implementation has no outer lambda though
# LOOP = (lambda x: x(x))(lambda x: x(x))
# beta reduces to itself!
LOOP_FACTORY = lambda _: (lambda x: x(x))(lambda x: x(x))

Y = lambda f: (lambda x: f(x(x)))(lambda x: f(x(x)))
# lets walk through the beta reduction of the Y combinator
# (lambda x: f(x(x)))(lambda x: f(x(x)))
# f (lambda x: f(x(x))( lambda x: f(x(x))))
# f ( f ( lambda x: f(x(x)) (lambda x: f(x(x))) ) )
# it keeps adding f in front. There we have recursion!

# the problem lies with x(x) which blows everything up
# so we defer the evaluation of it
# x is a function that takes one argument,
# so we do something called an eta expansion
# x ==becomes=> lambda v: x(v)
# see: https://wiki.haskell.org/index.php?title=Eta_conversion
Z = lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v)))


# UNTIL_ZERO = lambda n: IS_ZERO(n)(TRUE)(UNTIL_ZERO(PRED(n)))
#
# UNTIL_ZERO_F = lambda f: lambda n: IS_ZERO(n)(TRUE)()
#
# above code overloads the stack because python is eager
# look at the false branch f(PRED(n)) (henceforth denoted g)
# it is still being evaluated even if we want to return TRUE
# so we need to do another eta expansion
# g becomes lambda x: g(x)
UNTIL_ZERO_F = lambda f: lambda n: IS_ZERO(n)(TRUE)(lambda x: f(PRED(n))(x))
UNTIL_ZERO = Z(UNTIL_ZERO_F)


# FACTORIAL_F = lambda f: lambda n:\
#     IS_ZERO(n)\
#         (ONE)\
#         (TIMES(n)( f(SUB(n)(ONE)) ))
# again, need another eta expansion
# fmt: off
FACTORIAL_F = lambda f: lambda n:\
    IS_ZERO(n)\
        (ONE)\
        (TIMES(n)( lambda x: f(SUB(n)(ONE))(x) ))
# fmt: on
FACTORIAL = Z(FACTORIAL_F)


def eval_bool(x):
    return x(True)(False)


def eval_num(x):
    return x(lambda x: x + 1)(0)
