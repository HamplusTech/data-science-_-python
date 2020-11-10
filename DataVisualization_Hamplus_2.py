import matplotlib.pyplot as plt
a = [number for number in range(1,15,3)]
b = [number for number in range(1,15,2)]
plt.plot(range(1,6), a, 'o-', label='Odd')
plt.plot(range(1,8), b, 'o-', label='Even')
plt.xlabel('N')
plt.ylabel('M')
plt.legend()
plt.show()
