from MetodoDaBisseccao import metodo_bissecao
from MetodoDaFalsaPosicao import falsa_posicao
from MetodoDeNewton import metodo_newton
from MetodoDaSecante import metodo_secante

def captura_valores():
    """Captura coeficientes, intervalo e tolerância do usuário"""
    coef = list(map(float, input(
        "\nDigite os coeficientes de cada termo (ex.: 1 0 -1 -2, para x^3 - x - 2): "
    ).split()))

    a, b = map(float, input("Digite o intervalo que se encontra a raiz (ex.: 1 2): ").split())

    tol = float(input("Digite o fator de tolerância (ex.: 0.01): "))

    return coef, a, b, tol

def menu():
    print("""
Digite qual método você quer usar para resolver essa equação polinômial:

[1] Método da Bisseção
[2] Método da Falsa Posição
[3] Método de Newton
[4] Método da Secante
[q] Sair
""")

def executar_metodo(metodo_func, nome_metodo):
    print(f"\n{nome_metodo}")
    coef, a, b, tol = captura_valores()
    metodo_func(coef, a, b, tol)

if __name__ == "__main__":
    metodos = {
        '1': (metodo_bissecao, "Método da Bisseção"),
        '2': (falsa_posicao, "Método da Falsa Posição"),
        '3': (metodo_newton, "Método de Newton"),
        '4': (metodo_secante, "Método da Secante"),
    }

    menu()
    escolha = input("Opção: ").strip().lower()

    if escolha == 'q':
        print("Saindo...")
    elif escolha in metodos:
        func, nome = metodos[escolha]
        executar_metodo(func, nome)
    else:
        print("\nOpção inválida.")
