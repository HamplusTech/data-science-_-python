import numpy as np
import matplotlib.pyplot as plt
plt.plot(np.arange(10), np.arange(10), '*-',label='linear line')
plt.plot(np.arange(10), np.log(np.arange(10)),'o-',label='log line')
plt.plot(np.arange(10), np.sin(np.arange(10)), '.-',label='sin line')
plt.xlabel('Uniform')
plt.ylabel('Different')
plt.legend()
plt.show()
