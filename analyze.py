import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load("data/backleg_values.npy")

frontLegSensorValues = numpy.load("data/frontleg_values.npy")

matplotlib.pyplot.plot(backLegSensorValues,label='Back Leg',color='purple')

matplotlib.pyplot.plot(frontLegSensorValues,label="Front Leg", color='red')

matplotlib.pyplot.xlabel("Step Iteration")
matplotlib.pyplot.ylabel("Sensor Value")

matplotlib.pyplot.legend()
matplotlib.pyplot.show()