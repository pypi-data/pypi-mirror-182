import numpy as np

from forge_python import forge
sensor = forge.sensor()
sensor.authenticate('4c6915f5-5abb-4d29-a000-1ff589cff36e')

for value in np.linspace(95, 99.5, 50):
    sensor.send({'temperature': value})
