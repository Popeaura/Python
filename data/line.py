import matplotlib.pyplot as plt
import numpy as np

# Correct function name: linspace
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Line Plot of sin(x)')
plt.show()
