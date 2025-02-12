import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load("data/backleg_values.npy")

frontLegSensorValues = numpy.load("data/frontleg_values.npy")

matplotlib.pyplot.plot(backLegSensorValues,label='Back Leg',linewidth=5)

matplotlib.pyplot.plot(frontLegSensorValues,label="Front Leg")

matplotlib.pyplot.legend()
matplotlib.pyplot.show()