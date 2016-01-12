import numpy as np
import matplotlib.pyplot as plt
from math import pi
from math import e
from math import degrees
from math import radians



def h(energy):
    if energy == 'joule':
        return 6.62607004081*10-34
    else if energy == 'eV':
        return 4.13566766225*10**-15

def E(energy,v): return h(energy) * v

def Ew(energy, w): return (h(energy)/(2 * pi))(2*pi*w)

