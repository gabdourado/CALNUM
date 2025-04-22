# Implementação de Algoritmos Numéricos em Python

Este repositório contém a implementação em Python de algoritmos numéricos estudados em sala de aula. Atualmente, está incluído os seguintes métodos:

1. Método da Bissecção
2. Método da Falsa Posição

As implementações, até o momento, só calculam raizes de funções polinômiais. 😆

---

## 📌 Método da Bissecção

O Método da Bissecção é um algoritmo numérico que permite encontrar raízes de funções contínuas em um intervalo onde a função muda de sinal. Baseia-se no **Teorema do Valor Intermediário**, que garante a existência de uma raiz no intervalo.

### 🔎 Teorema do Valor Intermediário (Teorema de Bolzano)

> Se $f(x)$ for uma função contínua em um intervalo $[a, b]$ e $f(a)$ e $f(b)$ tiverem sinais opostos, ou seja, $f(a) \cdot f(b) < 0$, então existe pelo menos um ponto $c \in [a, b]$ tal que $f(c) = 0$.

### 🧮 Etapas do Método

1. **Escolha do Intervalo Inicial**: Defina um intervalo $[a, b]$ tal que $f(a) \cdot f(b) < 0$.

2. **Cálculo do Ponto Médio**: Calcule o Ponto Médio do intervalo $c = \frac{(a + b)}{2}$

3. **Teste da Raiz**:

- Se $f(a) \cdot f(c) < 0$, então a raiz está em $[a, c]$ → atualize $b = c$
- Se $f(a) \cdot f(c) > 0$, então a raiz está em $[c, b]$ → atualize $a = c$
- Se $f(c) = 0$, a raiz foi encontrada!

4. **Repetição**  
Repita o processo até que a diferença entre $b$ e $a$ seja menor que a precisão desejada ($ε$), ou seja, $|b - a| < ε$.

---

# 📌 Método da Falsa Posição

O Método da Falsa Posição (ou *Regula Falsi*) é uma variação do **Método da Bissecção**, mas tende a ser mais eficiente em alguns casos, pois utiliza uma reta secante entre dois pontos para estimar a raiz.

### 🧮 Etapas do Método

1. **Escolha do Intervalo Inicial**: Defina um intervalo $[a, b]$ tal que $f(a) \cdot f(b) < 0$.

2. **Cálculo do Ponto Médio**: Calcule o Ponto Médio do intervalo $c = \frac{(a + b)}{2}$

2. **Cálculo da Média “Pesada”**: Calcule o ponto $c$ como: $c = \frac{(a\cdot f(b) - b \cdot f(a))}{f(b) - f(a)}$

3. **Teste da Raiz**:

- Se $f(a) \cdot f(c) < 0$, então a raiz está em $[a, c]$ → atualize $b = c$
- Se $f(a) \cdot f(c) > 0$, então a raiz está em $[c, b]$ → atualize $a = c$
- Se $f(c) = 0$, a raiz foi encontrada!

4. **Repetição**  
Repita o processo até que a diferença entre $b$ e $a$ seja menor que a precisão desejada ($ε$), ou seja, $|f(c)| < ε$.

---
