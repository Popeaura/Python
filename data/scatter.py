import matplotlib.pyplot as plt
import numpy as np

x = np.random.random(100)

y = np.random.random(100)


plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('scatter plot of random data')
plt.show()