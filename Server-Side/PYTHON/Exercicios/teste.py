import matplotlib.pyplot as plt
import numpy as np

# Função de primeiro grau: f(x) = ax + b
def funcao_primeiro_grau(a, b, x):
    return a*x + b

# Função de segundo grau: f(x) = ax^2 + bx + c
def funcao_segundo_grau(a, b, c, x):
    return a*x**2 + b*x + c

# Intervalo de x
x = np.linspace(-10, 10, 400)

# Parâmetros das funções
a_primeiro_grau = 2
b_primeiro_grau = 1

a_segundo_grau = 1
b_segundo_grau = 2
c_segundo_grau = -1

# Calcula os valores de y para cada função
y_primeiro_grau = funcao_primeiro_grau(a_primeiro_grau, b_primeiro_grau, x)
y_segundo_grau = funcao_segundo_grau(a_segundo_grau, b_segundo_grau, c_segundo_grau, x)

# Plotagem dos gráficos
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(x, y_primeiro_grau)
plt.title('Função de Primeiro Grau')
plt.xlabel('x')
plt.ylabel('f(x)')

plt.subplot(1, 2, 2)
plt.plot(x, y_segundo_grau)
plt.title('Função de Segundo Grau')
plt.xlabel('x')
plt.ylabel('f(x)')

plt.tight_layout()
plt.show()

