Atoms and Electrons
===

2.2 Experimental Observations
---

**The photoelectric effect**
- blackbody radiation is emitted from heated samples, 
	- emitted in discrete units of energy called quanta
	- described by hv | v:=frequency of the radiation, h:= plancks constant

**Wave/Partical Duality**
- planks hypothesis and experiment
	- light energyy is contained in discrete units rather than in a continuous distribution of energies.
	- light has wave nature
		- but photons
			- quantized, localized units of light energy
	- photoelectron energy does not increase with light intensity
		- number of photoelectrons increases with intensity
		- higher intensity of light means more photons.  more photons hit electrons and free more photoelectrons
- youngs double slit experiment
	- diffraction and interference pattern is consistant with wave behavior
- De Broglie
	- particles of matter could also exhibit wave characteristics in some experiments
- Planck and De Broglie relationships are fundamental in quantum physics
	- valid for all situations and objects
	- connect wave description of phenomena (freq and wavelength) to particle description (energy and momentum)
		- dispersion relationship (relationship between freq and wavelength) not the same for different objects

**Atomic Spectra**
- energy is released from atoms with certain discrete energies

2.3 The Bohr Model
---
- relies on several postulates 
	- electrons exist in certain stable, circular orbits around the nucleus
		- implies the orbiting elecctron does not give off radiation, so it can keep its orbit
	- electron may shift to an orbit of higher or lower energy
		- thereby gaining or losing energy equal to the difference in energy levels
		- absorbing or emitting photons
	- angular momentum of the electron in an orbit is always an integral multiple of plancks constant divided by 2 Pi
		- necessary to get obvserved results from Paschen, Lyman, and Balmer, and was proposed just to make the data fit
		- inspired Schrodinger for his wave equation

2.4 Quantum Mechanics
===
- principles were developed from two different points of view at the same time
	- look different, but actually the same basic principles
- Heisenberg
	- *matrix mechanics* uses matrices
- Schrodinger
	- *wave mechanics* uses wave equation 

**Probability and the uncertainty principle**
- cant describe events on atomic scale with absolute precision
	- use expected values (averages) of position, momentum, and energy of particle
	- this is because absolute certainty doesnt exist on this scale.  
	- magnitude of the uncertainty is described by **Heisenberg uncertainty principle**
	- **simultaneous measurement of position and momentum, or of energy and time, is inherently inaccurate to some degree.**
	- cant look for *the* electron, but must find the *probability* of finding an electron at a certain position
		- use a probability density function for a particle in a certain environment to find expected values

**Schrodinger Wave Equation**
- Basic Postulates
	- Each particle in a physical system is described by a wavefunction Psi(x,y,z,t)
		- Psi and its derivative are continuous, finite, and single valued
	- When dealing with classical quantities like energy E and momentum p, we must relate these quantities with abstract quantum mechanical operators
	- The probability of finding a particle with wavefunction Psi in a volume dx dy dz is Psi Psi* dx dy dz
		- Psi Psi* is normalized so that the integral of Psi Psi* dx dy dz from negative infinity to positive infinity is 1
		- average value \<Q\> of some variable Q is calculated from the wavefunction by using operator form Q_op
			- \<Q\> = Integral of Psi\* Q_op Psi dx dy dz from negative infinity to positive infinity
		- the resulting equation includes both space and time dependencies
			- commonly the dependencies are calculated separately and then combined
- any arbitrary wavefunction can be written as a linear combination of the eigenfunctions
	- with pre-factors or weighting coefficients that depend on the initial conditions.

**Potential Well Problem**
- it's very difficult to find solutions to schrodinger equation for realistic situations, but there are problems that illustrate the theory
	- potential energy well with infinite boundaries 
	- V(x) = infinite for x = {0,L} else V(x) = 0
	- energy is quantized in the well.  Not continuous, and only certain values are allowed
		- these energy levels show up in lots of small-geometry structures in semiconductors
	- quantum state of the particle is described by {quantum number => energy state, wave function}
	  
	
2.5 Hydrogen Atom
---
- wave function requires a solution of schrodinger in 3 dimensions for a Coulombic potential field
	- V(x,y,z) => V(r, theta, phi) : V(r,theta,phi) = V(r) = q^2 /(-4 Pi epsilon_nought r)
	- psi(r,theta,phi) => R(r) THETA(theta) PHI(phi) : **time independent**
		- separated equations are then found in the three parts, and solving all three can get us psi
		- all three give us quantized solutions
		- quantum number then gets associated the each of the three parts
- atomic numbers
	- n : principle quantum number
		- specifies the orbit of the electron (shell)
	- m
	- l
	- s : magnetic spin
- all of the allowed states here show that an electron in a H atom can have a large number of possible excited states
	- these energy differences account for observed lines in H spectrum

**The Periodic Table**
- need to alter the above energy equations and wave functions to move beyond Hydrogen
- quantum number selection rules are valid for more complicated structures, 
	- use these rules to understand periodic table arrangement
- *Pauli exclusion principle*
	- no two electrons in an interacting system can have the same set of quantum numbers
	- no two electrons can occupy the same state
		- two electrons can have the same n,l,m, but they must have opposite spins
	- this is fundamental to electronic structure of all atoms in the table
		- we can determine which shell an electron fits, and how many electrons are allowed per shell
		- so this determines how many electrons a shell can borrow from another atom

			
Summary
===
- In classical physics, matter (including electrons) was described as *particles* by Newtonian mechanics, while *light* was described as waves, consistent with phenomena such as interference and diffractions of light.
- Phenomena such as blackbody radiation and the photoelecttric effect forced Planck and 
Einstein to introduce a *particle* aspect to light (photons).  Analysis of atomic spectra then led Bohr and de Broglie to analogously introduce a wave aspect to subatomic particles such as electrons.  This led to a *wave-particle duality* and a *quantum mechanical* description of nature by Heisenberg and Schrodinger.
- To understand how electrons move in semiconductor devices or interact with light, we need to determine a *complex wavefunction* of the electron.  The wave-function has to be mathematically well behaved, consisten with the interpretation that the *wavefunction magnitude squared is the probability density* of finding the electron in space and time.
- We get the wavefunction by solving Schrodinger's time-dependent partial differential equation.  The application of *boundary conditions* (the potential energy profile) allows certain (proper) *eigenfunctions* as valid solutions, with corresponding *eigenenergies*, determined by *allowed quantum numbers*.  Results of physical measurements are *no longer deterministic* (as in classical mechanics) but *probabilistic*, with an *expectation* value given by an average using the wavefunction of appropriate quantum mechanical *operators* corresponding to physical quantities.
- Application of these principles to the simplest atom (H) introduces four quantum numbers -- n,l,m,and s, which are subject to appropriate quantum mechanical rules.  Extrapolating these ideas to more complicated atoms such as Si leads to the idea of electronic structure and teh periodic table, if we apply the *Pauli exclusion principle* that one can have a maximum of one electron for one set of these quantum numbers.

