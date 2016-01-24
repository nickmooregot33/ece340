Crystal Properties and Growth of Semiconductors
===
1.1 Semiconductor materials
---
- conductivity of semiconductors can be varied over orders of magnitude by changes in temp, optical excitation, and impurity content
- found in column IV and neighboring columns of periodic table
- electronic and optical properties of semiconductors are strongly affected by impurity concentration
	- impurities are used to vary these properties over wide ranges for different applications
	- process of affective these concentrations is called doping

- Elemental semiconductors
	- composed of single species of atoms
	- Si (silicon) and GE (germanium) (column IV)
	- often used in transistors and diodes
- Compound semiconductors
	- more than one species of atoms
	- common combinations are from
		- III and V
		- II and VI
		- IV
	- common for high speed devices
	- common for light absorbption devices

-energy band gap
	- distinguish semiconductors from metals and insulators
 

1.2 Crystal Lattices
---
**Periodic Structures**
- atoms in a crystalline solid (crystal) are arranged periodically
	- knowing the basic periodicity, the solid appears exactly the same at multiple points
- not all solids are crystals
	- amorphous solids
		- no periodic structure at all
	- polycrystalline solids
		- many small regions of single-crystal material

- lattice
	- symmetric array of points
		- this symmetry determines the lattice, not the magnitude of the base vectors
	- defines the periodicity of a crystal
	- basis
		- can be one or more arranged atoms
		- one basis at each lattice point

	- primitive cell
		- cell is a pattern of lattice points that represents the entire lattice
		- this pattern is repeated throughout the lattice
		- primitive cell is the smallest such cell
		- is not unique
		- must cover exactly the entire volume of the crystal
		- lattice points are shared (split evenly) between cells which use them
		- primitive cells can be found in many shapes and sizes
		- lattice points are only at corners in the primitive cell
	- unit cell
		- often more convenient to use than the primitive cell
		- differently shaped from the primitive cell
		- lattice points can also be at face and body centers of a unit cell
	- lattice constant
		- 

**Cubic Lattices**
- simplest three dimensional lattice
- unit cell is a cube
	- atom at each corner of the unit cell => simple cubic structure
		- has 1 full atom per cube 
			- each corner atom is shared with 8 different cubes
	- atom centered at each face of cube and at each corner=> face-centered cubic
		- has 4 full atoms per cube
			- each corner atom is shared 8 ways (total of 1)
			- each face atom is shared 2 ways (total of 3)
	- atom at center of cuber and at each corner=> body-centered cubic
		- has 2 full atoms per cube
			- the 8 corner atoms split 8 ways each
			- the center atom the cube does not share

**Planes and Directions**
- need to describe directions and/or planes within a lattice
	- use an xyz coordinate plane
	- origin at any lattice point
	- axes line up with edges of cubic unit cell
- directions are similar to standard cartesian system vectors
- Miller Indices define a particular plane in the lattice
	- to find the Miller indices
		- find intercepts of plane with crystal axes and put in terms of integral multiples of the base vectors
		- take the reciprocals of the three integral multiples -- mulitply the set by some factor to get the smallest set of integers which have the same relationship to each other
			- this is difficult to explain, and the book describes it poorly
		- these new integers are h, k, and l
		- our plane is now described by (hkl)
	- many planes are equivalent when describing crystals
		- can rotate and change position of unit cell to change description of a plane
			- rotating a simbple cubic unit cell shows that we can call each plane the same Miller indices
		- (hkl) becomes {hkl} to describe the set of all equivalent planes described by h,k, and l
- describing a direction
	- set of 3 integers with same relationship as components of a vector in that direction
		- expressed in multiples of basis vectors
		- reduced to smallest integers keeping the same relationship between them
		- for integers a,b,and c describing the direction, we write [abc]
		- for equivalent directions we write <abc>
- [hkl] is perpendicular to (hkl)

**Diamond Lattice**
- basic cryystal structure for many important semiconductors
- fcc with basis of two atoms (face-centered cubic with basis of two atoms)
	- Si, Ge, and C in diamond form
	- fcc lattice with an extra atom placed at a/4 + b/4 + c/4 from each of the fcc atoms
	- so there are 2 interpenetrating fcc sublattices displaced by <1/4,1/4,1/4> vector
- zinc-blend
	- many compound semiconductors
		- typical of the III-V compounds
	- basic diamond structure, but different atoms on many sites
- III-V compounds
	- have the abililty to vary mixture of elements on each of the two sublattices of zinc blend crystal
	- common to represent the composition by assigning subscripts to the various elements
	- subscripts of a interpenetrating lattice add up to 1
- each atom in diamond and zinc-blend have 4 nearest neighbors
	- this is important for fabrication
1.3 Bulk Crystal Growth
===
- This is a bunch of stuff I'm not going to read, I think

1.4 Epitaxial Growth
===

1.4.1 Lattice matching in epitaxial growth 
---

1.5 Wave Propagation in discrete periodic structures
===
- wave is described by wavelength, 
	- angular frequency 
	- phase 
	- intensity I = A^2 
	- v_p is phase velocity and can be written w/k
- may deal with a wave packet
	- made up of a superposition of various waves
	- can be shown to travel with *group velocity* v_g
	- v_g = dw/dk
	- psi = A e^(j(kx +/- st)) describes a plane wave
		- also, one can take linear combinations of these plane waves and describe them as standing waves
			 - sin(kx +/- wt) and/or cos(kx +/- wt)
	- plane waves can't travel in a finite crystal
		- reflections at the boundaries will cause standing wave patterns
	- math is simpler for infinite crystal
		- psi(0) = psi(L) (periodic boundary condition)

Summary
===
- Semiconductor devices are at the heart of information technology.  Elemental semiconductors such as Si appear in column IV of the periodic table, while compound semiconductors such as GaAs consist of elements symmetrically around column IV.  More complicated alloy semiconductors are used to optimize optoelectronic properties.
- These devices are generally made in single-crystal material for best performance.  Single crystals have long-range order, while polycrystalline and amorphous materials have short-range and no order, respectively.
- Lattices are determined by symmetry. In 3-D, these are called Bravais lattices.  When we put a basis of atom(s) on the lattice sites, we get a crystal.  Common semiconductors have an fcc symmetry with a basis of two identical or different atoms, resulting in diamond or zinc blende crystals, respectively.
- The fundamental building block of a lattice is a primitive cell with lattice points at its corners.  Sometimes it is easier to describe the crystal in terms of a larger "unit" cell with lattice points not only at the corners but also at body or face centers.
- Translating unit cells by integer numbers of basis vectors can replicate the lattice.  Planes and directions in a lattice can be defined in terms of Miller indices.
- Real crystals can have defects in 0-,1-,2-, and 3-D, some of which are benign, but many of which are harmful for device operation.
- Semicontuctor bulk crystals are grown from a melt by the Czochralski method, starting from a seed.  Single-crystal epitaxial layers can be grown on top of semiconductor wafers in various ways, such as VPE, metal-organic chemical vapor deposition (MOCVD), or MBE.  One can thereby optimize doping and band-structure properties for device fabrication.

