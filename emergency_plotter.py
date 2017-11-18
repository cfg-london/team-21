import matplotlib.pyplot as pyplot
import matplotlib.colors
from mpl_toolkits.mplot3d import Axes3D
import numpy
import multiVariate

t, w, x, y, z = multiVariate.one_country_all_groups('Married women currently using any method of contraception', 'Colombia')

pyplot.figure()
pyplot.scatter(t, w)
pyplot.scatter(t, x)
pyplot.scatter(t, y)
pyplot.scatter(t, z)
pyplot.show()
