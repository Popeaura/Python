import matplotlib.pyplot as plt
import numpy as np

data = np.random.random(1000)

plt.hist(data, bins=30)
plt.xlabel('value')
plt.ylabel('Frequency')  # Corrected this line
plt.title('Histogram of random data')
plt.show()
