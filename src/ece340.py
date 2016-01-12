import numpy as np
import matplotlib.pyplot as plt
from math import pi
from math import e
from math import degrees
from math import radians



def h(energy):
    if energy == 'joule':
        return 6.62607004081*10E-34
    elif energy == 'eV':
        return 4.13566766225*10E-15

def E(energy,v): return h(energy) * v

def Ew(energy, w): return (h(energy)/(2 * pi))(2*pi*w)

if __name__ == '__main__':
    print h('joule')
    print h('eV')
    print E('joule',1000)

