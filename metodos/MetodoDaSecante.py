""" NOTA: É importante perceber que o método só funciona para funções do polinômiais """

from prettytable import PrettyTable
from math import fabs

def f(x, *coeficientes):
    valor = 0
    grau = len(coeficientes) - 1

    for i, coef in enumerate(coeficientes):
        valor += coef * x ** (grau - i)

    return valor

def calcula_novo_x(x_anterior, x_atual, f_anterior, f_atual):
  x = ((f_atual * x_anterior) - (f_anterior * x_atual) )/(f_atual - f_anterior)
  return x

def calcula_erro(x_anterior, x_atual):
  erro = fabs((x_atual - x_anterior) / x_atual) if x_atual != 0 else fabs(x_atual - x_anterior)
  return erro

def metodo_secante(coef, a, b, tol):

    x_anterior, x_atual = a, b

    f_anterior  = f(x_anterior, *coef)
    f_atual = f(x_atual, *coef)

    if f_anterior*f_atual > 0:
        print("Verifique se segue o Teorema de Bolzano.")
        return

    erro, num = 100, 1

    tabela = PrettyTable()

    tabela.field_names = ["n", "x(n)", "f(x(n))","tolerancia"]
    
    tabela.add_row([0, x_anterior, f_anterior, '-'])

    tabela.add_row([1, x_atual, f_atual, '-'])

    while erro >= tol:
        
        x_novo  = calcula_novo_x(x_anterior, x_atual, f_anterior, f_atual)
        
        f_novo = f(x_novo, *coef)

        num += 1
        
        erro = calcula_erro(x_anterior, x_atual)

        tabela.add_row([num, f"{x_novo:.6}", f"{f_novo:.6}", f"{erro:.6}"])

        x_anterior, f_anterior = x_atual, f_atual
        x_atual, f_atual = x_novo, f_novo

    print(tabela)

    print(f"\nA raiz aproximada é {x_novo} após {num} iterações com 𝜀 = {tol}")

if __name__ == "__main__":

    coef = list(map(float, input("Digite os coeficientes de cada termo (ex.: 1 0 -1 -2, para x^3 - x - 2): ").split()))

    a, b = map(float, input("Digite o intervalo (ex.: 1 2): ").split())

    tol = float(input("Digite o fator de tolerância (ex.: 0.01): "))

    metodo_secante(coef, a, b, tol)