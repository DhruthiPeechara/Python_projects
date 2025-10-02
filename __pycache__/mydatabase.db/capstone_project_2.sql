import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)  # 100 points from 0 to 10
y = np.sin(x)

plt.figure(figsize=(8, 6))
plt.plot(x, y, label='sin(x)', color='b', linewidth=2)

plt.bar(bar_x, bar_y, width=0.2, color='orange', alpha=0.6, label='Bar Plot (sin(x

plt.title('Sine Wave', fontsize=16)
plt.xlabel('x', fontsize=12)

plt.ylabel('sin(x)', fontsize=12)

plt.grid(True)

plt.legend()

plt.show()