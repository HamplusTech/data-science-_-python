print("Using Raw Python")

DATA = [
    ('Jones', 'Jane', 58),
    ('Smith', 'Anne', 30),
    ('Jones', 'Fred', 30),
    ('Smith', 'John', 60),
    ('Smith', 'Fred', 30),
    ('Jones', 'Anne', 30),
    ('Smith', 'Jane', 58),
    ('Smith', 'Twin2', 3),
    ('Jones', 'John', 60),
    ('Smith', 'Twin1', 3),
    ('Jones', 'Twin1', 3),
    ('Jones', 'Twin2', 3)
]

for tup in DATA:
    print("{:10s} {:10s} {}".format(*tup))


print("Using Pandas and Numpy")
import numpy as np
import pandas as pd

data = pd.DataFrame([('Jones', 'Jane', 58), ('Smith', 'Anne', 30), ('Jones', 'Fred', 30),
		     ('Smith', 'John', 60), ('Smith', 'Fred', 30), ('Jones', 'Anne', 30),
		     ('Smith', 'Jane', 58), ('Smith', 'Twin2', 3), ('Jones', 'John', 60),
		     ('Smith', 'Twin1', 3), ('Jones', 'Twin1', 3), ('Jones', 'Twin2', 3)],
		    index=[list(range(12))], columns= ["Last Name", "First Name", "Age"])
print(data)
