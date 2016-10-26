print('hellow world and i like chicken') #here i add some useless comments


print('blablalalalalala')

import matplotlib.pyplot as plt

plt.axes()

circle = plt.Circle((0, 0), radius=0.75, fc='y')
plt.gca().add_patch(circle)

plt.axis('scaled')
plt.show()



from math import pi
import numpy as np

def circunference(r):
    from math import pi
    return 2*r*pi

def areac(r):
    return pi*r**2
