'''import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 100)


y = 2 * x + 1

plt.figure(figsize=(8, 6))
plt.plot(x, y, label='y = 2x + 1', color='blue')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfico da função de segundo grau y = 2x + 1')
plt.grid(True)
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.xticks(np.arange(-10, 10, 1))
plt.yticks(np.arange(-10,10, 1))
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.legend()

plt.savefig('teste3.png')
plt.show()
'''

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 2, 100)
y = -x + 2

plt.figure(figsize=(8, 6))
plt.plot(x, y, label='y = -x + 2', color='blue')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfico da função y = -x + 2')
plt.xticks(np.arange(-2, 3, 1))
plt.yticks(np.arange(-2, 5, 1))
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.savefig('testee.png')
plt.show()