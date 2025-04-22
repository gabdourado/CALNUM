""" NOTA: É importante perceber que o método só funciona para funções do polinômiais """

from prettytable import PrettyTable

from math import fabs

nome_metodo1 = r""" 
___  ___         _                 _         
|  \/  |        | |               | |        
| .  . |   ___  | |_    ___     __| |   ___  
| |\/| |  / _ \ | __|  / _ \   / _` |  / _ \ 
| |  | | |  __/ | |_  | (_) | | (_| | | (_) |
\_|  |_/  \___|  \__|  \___/   \__,_|  \___/ 
"""
nome_metodo2 = r""" 
    _           ______         _                  ______                _                        
   | |          |  ___|       | |                 | ___ \              (_)                       
 __| |   __ _   | |_    __ _  | |  ___    __ _    | |_/ |  ___    ___   _    ___    __ _    ___  
/ _` |  / _` |  |  _|  / _` | | | / __|  / _` |   |  __/  / _ \  / __| | |  / __|  / _` |  / _ \ 
| (_|| | (_| |  | |   | (_| | | | \__ \ | (_| |   | |    | (_) | \__ \ | | | (__  | (_| | | (_) |
\__,_|  \__,_|  \_|    \__,_| |_| |___/  \__,_|   \_|     \___/  |___/ |_|  \___|  \__,_|  \___/ 
"""

def f(x, *coeficientes):
    valor = 0
    grau = len(coeficientes) - 1

    for i, coef in enumerate(coeficientes):
        valor += coef * x ** (grau - i)

    return valor

def calculaC(a, b, fa, fb):
  c = (a*fb - b*fa)/(fb - fa)
  return c

def prod(fa, fc):
    if fa * fc < 0: return -1
    elif fa * fc > 0: return 1 
    else: return 0 

def sinal(fa, fb):
  if fa * fb < 0: return '-'
  elif fa * fb > 0: return '+'
  else: return '0'


def falsa_posicao(coef, a, b, tol):

    fa  = f(a, *coef)
    fb = f(b, *coef)

    if fa*fb > 0:
        print("Raiz não está nesse intervalo! Verifique se segue o Teorema de Bolzano.")
        return

    erro, num = 100, -1

    tabela = PrettyTable()

    tabela.field_names = ["n", "a", "b", "c", "f(a)", "f(b)", "f(c)", "f(a)*f(c)","|f(c)|"]

    while erro >= tol:

        fa  = f(a, *coef)
        fb = f(b, *coef)

        c = calculaC(a, b, fa, fb)
        fc = f(c, *coef)

        v = prod(fa, fc)
        sin = sinal(fa, fc)

        num += 1
        erro = fabs(fc)

        tabela.add_row([num, f"{a:.6f}", f"{b:.6f}", f"{c:.6f}", f"{fa:.6f}", f"{fb:.6f}", f"{fc:.6f}", sin, f"{erro:.6f}"])

        if v < 0: b = c
        elif v > 0: a = c
        else: break

    print(tabela)

    print(f"\nA raiz aproximada é {c} após {num} iterações com 𝜀 = {tol}")

if __name__ == "__main__":
   
    print(nome_metodo1, end = '')
    print(nome_metodo2)

    coef = list(map(float, input("Digite os coeficientes de cada termo (ex.: 1 0 -1 -2, para x^3 - x - 2): ").split()))

    a, b = map(float, input("Digite o intervalo (ex.: 1 2): ").split())

    tol = float(input("Digite o fator de tolerância (ex.: 0.01): "))

    falsa_posicao(coef, a, b, tol)