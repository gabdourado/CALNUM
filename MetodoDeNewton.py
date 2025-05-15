""" NOTA: É importante perceber que o método só funciona para funções do polinômiais """

from prettytable import PrettyTable
from math import fabs

def f(x, *coeficientes):
    valor = 0
    grau = len(coeficientes) - 1

    for i, coef in enumerate(coeficientes):
        valor += coef * x ** (grau - i)

    return valor

def derivada(x, *coeficientes):
    valor = 0.0
    grau = len(coeficientes) - 1

    for i, coef in enumerate(coeficientes):
        exp = grau - i
        if exp > 0:
            valor += (grau - i) * coef * x ** (exp - 1)

    return valor

def calcula_novo_x(x_atual, f_atual, derivada_x):
    if derivada_x == 0:
        raise ZeroDivisionError("Derivada é zero! Método de Newton-Raphson falhou.")
    return x_atual - (f_atual) / derivada_x

def calcula_erro(x_novo, x_anterior):
  erro = fabs((x_novo - x_anterior) / x_novo) if x_novo != 0 else fabs(x_novo - x_anterior)
  return erro

def metodo_newton(coef, a, b, tol):

    fa = f(a, *coef)
    fb = f(b, *coef)

    if fa*fb > 0:
        print("Raiz não está nesse intervalo! Verifique se segue o Teorema de Bolzano.")
        return
    
    x_atual = (a + b) / 2

    f_atual = f(x_atual, *coef)

    derivada_atual = derivada(x_atual, *coef)

    erro, num = 100, 0

    tabela = PrettyTable()

    tabela.field_names = ["n", "x(n)", "f(x(n-1))","f'(x(n-1))", "tolerancia"]

    tabela.add_row([0, x_atual, '-', '-', '-'])

    while erro >= tol:
        
        x_novo  = calcula_novo_x(x_atual, f_atual, derivada_atual)

        num += 1
        
        erro = calcula_erro(x_novo, x_atual)

        tabela.add_row([num, f"{x_novo:.6}", f"{f_atual:.6}", f"{derivada_atual:.6f}", f"{erro:.6}"])
        
                
        f_novo = f(x_novo, *coef)
        derivada_nova = derivada(x_novo, *coef)

        x_atual, f_atual, derivada_atual = x_novo, f_novo, derivada_nova

    print(tabela)

    print(f"\nA raiz aproximada é {x_novo} após {num} iterações com 𝜀 = {tol}")

if __name__ == "__main__":
    
    coef = list(map(float, input("Digite os coeficientes de cada termo (ex.: 1 0 -1 -2, para x^3 - x - 2): ").split()))

    a, b = map(float, input("Digite o intervalo (ex.: 1 2): ").split())

    tol = float(input("Digite o fator de tolerância (ex.: 0.01): "))

    metodo_newton(coef, a, b, tol)