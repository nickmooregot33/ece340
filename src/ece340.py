import numpy as np
import matplotlib.pyplot as plt
from math import pi
from math import e
from math import degrees
from math import radians

avogadro = 6.02e23
atomic_weights = {
		'Si':28.085,
		'Ga':69.723,
		'As':74.922,
		'GaAs':144.645
		}

lattice_constants = { 		##in angstroms
		'Si':5.43,
		'GaAs':5.65
		}

def h(energy):
    if energy == 'joule':
        return 6.62607004081e-34
    elif energy == 'eV':
        return 4.13566766225E-15

def E(energy,v): return h(energy) * v

def Ew(energy, w): return (h(energy)/(2 * pi))(2*pi*w)

if __name__ == '__main__':
    print h('joule')
    print h('eV')
    print E('joule',1000)

