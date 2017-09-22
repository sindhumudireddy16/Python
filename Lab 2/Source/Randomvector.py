import numpy as np
Randomvector = np.random.random(15)
Randomvector[Randomvector.argmax()]=100
print(Randomvector)