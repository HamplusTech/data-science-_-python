f = open(r'C:\Users\HampoJohnPaulAC\Documents\CorelDRAW Graphics Suite X7.txt')
data = f.read()
f.close()

print(data)
print(f)

with open(r'C:\Users\HampoJohnPaulAC\Documents\CorelDRAW Graphics Suite X7.txt') as f:
    print(f.read())
print(f)
