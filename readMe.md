# Implementação de Algoritmos Numéricos em Python

Este repositório contém a implementação em Python de algoritmos numéricos estudados em sala de aula. Atualmente, está incluído os seguintes métodos:

1. **Método da Bissecção**
2. **Método da Falsa Posição**

As implementações, até o momento, só calculam raizes de funções polinômiais, com objetivo de ser ampliado para demais funções no futuro. 
---

## 📌 Método da Bissecção

O Método da Bissecção é um algoritmo numérico que permite encontrar raízes de funções contínuas em um intervalo onde a função muda de sinal. Baseia-se no **Teorema do Valor Intermediário**, que garante a existência de uma raiz no intervalo.

### 🔎 Teorema do Valor Intermediário

> Se `f(x)` for uma função contínua em um intervalo fechado `[a, b]` e `f(a) * f(b) < 0`, então existe pelo menos um ponto `c` em `[a, b]` tal que `f(c) = 0`.

---

### 🧮 Etapas do Método

1. **Escolha do Intervalo Inicial**  
   Defina um intervalo `[a, b]` tal que `f(a) * f(b) < 0`.

2. **Cálculo do Ponto Médio**  
   Calcule o ponto médio `c` do intervalo:
   `c = \frac{(a + b)}{2}`


3. **Teste da Raiz**  
Verifique o sinal de `f(c)`:
- Se `f(a) * f(c) < 0`, então a raiz está em `[a, c]` → atualize `b = c`
- Se `f(a) * f(c) > 0`, então a raiz está em `[c, b]` → atualize `a = c`
- Se `f(c) = 0`, a raiz foi encontrada!

4. **Repetição**  
Repita o processo até que a diferença entre `b` e `a` seja menor que a precisão desejada (`ε`), ou seja, `|b - a| < ε`

