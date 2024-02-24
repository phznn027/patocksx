import matplotlib.pyplot as plt
import numpy as np

# Definindo o intervalo de x
x = np.linspace(-10, 11, 100)

# Definindo a função y = 2x - 1
y = 2 * x + 1

# Configurando o gráfico
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='y = 2x + 1', color='blue')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfico da função de segundo grau y = 2x + 1')
plt.grid(True)
plt.xlim(-10, 11)
plt.ylim(-10, 11)
plt.xticks(np.arange(-10, 11, 1))
plt.yticks(np.arange(-10,11, 1))
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.legend()

# Mostrando o gráfico
plt.savefig('teste3.png')
plt.show()
