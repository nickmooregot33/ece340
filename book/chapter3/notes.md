Energy Bands and Charge Carriers in Semiconductors
===	       
3.1 Bonding Forces and Energy Bands in Solids
--- 
- electrons in solids are restricted to certain energies and are not allowed at other energies.  
	- has range of *band* of energies allowed per electron due to overlapping of wave functions of other electrons -- Pauli exclusion

**Bonding forces in solids**
- ionic bonding
	- mechanisms for alcali halides (alkali are the far left metals (one loose electron), halogens are just left of noble gases (one empty spot))
		- metal gives up its extra electrons to the nonmetal
		- the crystal then has structure of noble gases
		- but the ions have net electric charges which then act on all of the oppositely charged nearest neighbors, pulling them in tight.
		- all electrons are tightly bound to atoms, and are difficult to separate (relatively) => insulator
			- outer orbits are completely filled
			- no loosely bound outer orbiting electrons.  only filled shells
- metallic bonding
	- outer electron of each alkali atom is given to the crystal as a whole
	- solid is a bunch of ions with closed shells surrounded by a sea of free electrons
		- electrons are free to move around the crystal when influenced by electric field
		- lattice is held together by interaction of positive ion cores and surrounding free electrons

- covalent bonding
	- in the diamond lattice semiconductors (Ge, Si, C)
	- each atom shares its 4 outer electrons (valence electrons) with its four nearest neighbors 
		- bonding forces come from quantum mechanical interactions
		- each electron pair is a covalent bond, both electrons belong to the bond, not to a specific atom
			= each electron in a bond is indistinguishable, except with opposite spin to satisfy Pauli exclusion
	- no free electrons per se but electrons can be excited out of a bond
	- for compound semiconductors
		- mixed bonding - both ionic and covalent bonding
		- ionic bonding is affected by the separation in columns on the periodic table
			- becomes more important as the distance between the two elements increases

**Energy Bands**
- LCAO (Linear combinations of atomic orbitals)
	- wave function for two electrons on neighboring atoms can be superposed
	- form antibonding orbital and bonding orbital
		- bonding orbital corresponds to covalent bond
	- parallel spins repel each other => they go to antibonding states, opposite for antiparallel spins
	- can have many more than two interacting wave functions, orbitals => energy bands
	- lowest energy levels are for bonding, higher energy levels are for antibonding

**Direct and Indirect Semiconductors**
- direct semiconductors can have electrons fall from conduction band to valence band while keeping k constant
- indirect semiconductors must change k to switch bands for an electron
	- must change momentum and energy
	- generally, when involving a change of k, part of the energy is given up as heat to the lattice
- differences between direct and indirect semiconductors is important for choosing semiconductors with light output
           	- LEDs and lasers need direct transitions or indirect but vertical transitions that use defect states 
		- give up the extra energy as a photon

**variation of energy bands with alloy composition**
- varying the compounds within a lattice (with a percentage of the groupX compounds being one element, and the rest being another) has an effect on energy band structures
- alloys can change from indirect to direct or vice versa by varying the percentages

3.2 Charge Carriers in Semi-Conductors
---
**Electrons and Holes**
- At 0K, all electrons are in valence band.  As temperature rises some electrons are excited into the conduction band by receiving enough thermal energy
  - resulting in a *mostly* filled valence band and a few electrons in conduction band, and a **crapload** of empty states in the conduction band
- empty state in the valence band is a **hole**
  - **electron-hole pair (EHP)** is an electron excited to conduction band from valence band, and the hole it leaves behind
  - electrons in conduction band are free to move around easily
  - current contribution of a hole is equivalent to that of a positively charged particle with velocity v_p (the same as the missing electron)

**Effective Mass**
- electrons in a crystal are not free from interaction with the lattice
  - wave-particle motion is different from e^- in free space
  - therefore e^-s have an altered values of particle mass
  - effective mass calculations have to take 3D shape of energy bands into account
    - curvature of the band determines the e^- effective mass
      - electrons with negative charge and negative mass move with the electric field in the valence band => just like the holes they are modeling
      - the curvature changes based on k, so we have varying electron effective masses based on what direction we are going in the crystal
      	- longitudinal effective mass along the major axis, and two transverse effective masses along the minor axes
- effective mass values need to be selected based on the material in question

**Intrinsic Material**
- intrinsic semiconductors are perfect crystals with no impurities or lattice defects
- no charge carriers at 0K
- higher temps => EHPs are generated 
- EHPs are the only charge carriers in an intrinsic crystal
- conduction band electron numbers are equal to number of valence band holes
- n_i is the number of holes or the number of electrons in the bands for intrinsic material
  - r_i is the recombination rate
  - g_i is the generation rate
  - all are measured in \frac{EHP}/{cm^3} and all are temperature dependent

**Extrinsic Material**
- doping creates extrinsic material by purposely introducing impurities into the crystal
- 2 types, n-type and p-type
  - n-type adds electrons to the conduction band
  - p-type adds holes to the valence band
- extrinsic  material is when n_0 and p_0 are different from n_i
- impurities create new energy levels, usually in the band gap
  - donor level
    - created near the conduction band.  It's full at 0K, but as temperature rises, almost all of the electrons jump to conduction band
    - column V atoms are generally donor impurities for Ge and Si.  They have 5 electrons in the outer shell, so when they fill Column IV slots as impurities, they end up having an extra electron crammed in, that usually releases easily
  - acceptor level
    - created near the valence band.  It's empty at 0K, but as temperature rises electrons jump into the acceptor level, leaving holes behind
    - atoms from column III are acceptor impurities in Ge and Si, as they only have 3 valence electrons, leaving an incomplete bond
- amphoteric impurities
  - can serve as donors or acceptors depending on which sublattices they are  sitting in
- when doping, one type of carrier usually dominates, called the *majority carrier*, and the other one is the *minority carrier.*

3.3 Carrier Concentrations
---
- Fermi Level
  - f(e) gives probability an __*available*__ energy state at E will be occupied by an electron at absolute temperature T
    - f(E) is probability states above E_F is filled
    - 1-f(E) is probability states below E_F is empty
  - E_f is the fermi level

**Electron and Hole Concentrations at Equilibrium
- Lots of Equations

**Temperature Dependence of Carrier Concentrations**
- The temperature dependence dominates the other dependencies when calculating the intrinsic carrier concentration
- Up until a certain temperature (starting from 0K) the donor atoms get ionized (ionization region)
- once the threshold for all donor atoms being ionized is reached, n_0 stays constant at the number of donors and the device is extrinsic
- when temperature gets to another point, the intrinsic carrier begin to outnumber the donor atoms, and the device becomes intrinsic again
  - most of the time this is avoided by making sure the temperature range of operation is below this temperature

**Compensation and Space Charge Neutrality**
- often enough, the device has both donors and acceptors.  How to calculate?
- conduction band electrons end up filling the acceptor holes, reducing n_0 from N_d
- 