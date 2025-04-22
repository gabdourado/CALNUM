""" NOTA: É importante notar que o método só funciona para funções do polinômiais """

from prettytable import PrettyTable

from math import fabs

metodo = r"""
___  ___         _                 _                _           ______   _                                           
|  \/  |        | |               | |              | |          | ___ \ (_)                                          
| .  . |   ___  | |_    ___     __| |   ___      __| |   __ _   | |_/ /  _   ___   ___    ___    ___    __ _    ___  
| |\/| |  / _ \ | __|  / _ \   / _` |  / _ \    / _` |  / _` |  | ___ \ | | / __| / __|  / _ \  / __|  / _` |  / _ \ 
| |  | | |  __/ | |_  | (_) | | (_| | | (_) |  | (_| | | (_| |  | |_/ / | | \__ \ \__ \ |  __/ | (__  | (_| | | (_) |
\_|  |_/  \___|  \__|  \___/   \__,_|  \___/    \__,_|  \__,_|  \____/  |_| |___/ |___/  \___|  \___|  \__,_|  \___/ 
"""

def f(x, *coeficientes):
    valor = 0
    grau = len(coeficientes) - 1

    for i, coef in enumerate(coeficientes):
        valor += coef * x ** (grau - i)

    return valor

def media(a, b):
    return (a + b) / 2

def prod(fa, fc):
    if fa * fc < 0: return -1
    elif fa * fc > 0: return 1
    else: return 0

def sinal(fa, fc):
  if fa * fc < 0: return '-'
  elif fa * fc > 0: return '+'
  else: return '0'

def bissecao(coef, a, b, tol, erro = 100, num = -1):

    fa  = f(a, *coef)
    fb = f(b, *coef)

    if fa*fb > 0:
        print("Raiz não está nesse intervalo! Verifique se segue o Teorema de Bolzano.")
        return

    tabela = PrettyTable()

    tabela.field_names = ["n", "a", "b", "c", "f(a)", "f(b)", "f(c)", "f(a)*f(c)","tolerancia"]

    while erro >= tol:

        fa  = f(a, *coef)
        fb = f(b, *coef)

        c = media(a, b)
        fc = f(c, *coef)

        v = prod(fa, fc)
        sin = sinal(fa, fc)

        num += 1
        erro = fabs(a - b)

        tabela.add_row([num, f"{a:.6f}", f"{b:.6f}", f"{c:.6f}", f"{fa:.6f}", f"{fb:.6f}", f"{fc:.6f}", sin, f"{erro:.6f}"])

        if v < 0: b = c
        elif v > 0: a = c
        else: break

    print(tabela)
    print(f"A raiz aproximada é {c} após {num} iterações com 𝜀 = {tol}")

if __name__ == "__main__":

    print(metodo)

    coef = list(map(float, input("Digite os coeficientes de cada termo (ex.: 1 0 -1 -2, para x³ - x - 2): ").split()))

    a, b = map(float, input("Digite o intervalo onde se encontra a raiz (ex.: 1 2): ").split())

    tol = float(input("Digite o fator de tolerância (ex.: 0.01): "))

    bissecao(coef, a, b, tol)