"""
    Exercício 07

    Defina uma função recursiva que calcule o maior divisor comum (M.D.C) entre dois número a e b, em que a > b.

mdc(a, b) = {
    a                       b = 0
    mdc(b, a - b [a / b])   a > b
}

Em que a - b[a / b] pode ser escrito em Python como: a % b.
"""

def mdc(a, b):
    if b == 0:
        return a
    elif a > b:
        return mdc(b, a % b)


print(mdc(40, 12))
