import matplotlib.pyplot as plt
import numpy as np


calorias = [
    250, 790, 470, 510, 500, 330,
    300, 750, 580, 740, 420, 260,
    440, 770, 400, 540, 530, 330,
    390, 380, 340, 460, 530, 260,
    410, 360, 270, 510, 630, 330
]


plt.figure(figsize=(10, 6))
plt.hist(calorias, bins=6, edgecolor='black')
plt.xlabel('Calorías')
plt.ylabel('Frecuencia')
plt.title('Histograma de calorias de alimentos :sandwich')
plt.savefig('histograma.png')
plt.show()


calorias_sorted = sorted(calorias)


frecuence = np.arange(1, len(calorias) + 1) / len(calorias)


plt.figure(figsize=(10, 6))
plt.plot(calorias_sorted,frecuence, marker='o', linestyle='-')
plt.xlabel('Calorías')
plt.ylabel('Frecuencia acumulada')
plt.title('Ojiva de calorias de alimentos :sandwich')
plt.grid(True)
plt.savefig('ojiva.png')
plt.show()
