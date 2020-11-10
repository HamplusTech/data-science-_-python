import numpy as  np
import matplotlib.pyplot as plt
x_data = np.arange(-4,6)
cdata = np.cos(x_data)
sdata = np.sin(x_data)
tdata = np.tan(x_data)
plt.plot(x_data, sdata,'*-',label='Sin Curve')
plt.plot(x_data, cdata, '.-', label='Cos Curve')
plt.plot(x_data, tdata, 'o-', label='Tan Curve')
plt.title('Sin, Cos and Tan Plot Comparison')
plt.xlabel('X_data (Uniform)')
plt.ylabel('Y_data (All Data)')
plt.legend(['Sin', 'Cos', 'Tan'])
plt.show()
