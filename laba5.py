from enum import Enum 
class Atom:
    """
    Represents an atom with basic properties.
    """
    def __init__(self, name='', atomic_mass_unit=0, neutrons_number=0, protons_number=0, electrons_number=0):
        """
        Initialize an Atom object.
        """
        self.name = name
        self.atomic_mass = atomic_mass_unit
        self.neutrons = neutrons_number
        self.protons = protons_number
        self.electrons = electrons_number
    
    def isNeutral(self):
        """
        Check if the atom is neutral."""
        return self.neutrons + self.electrons == self.protons

class TypeStatus(Enum):
    """
    Enumeration representing different types of atom status.
    """
    ISOTYPE = 1
    RADIOACTIVE = 2
    ION = 3
    ANTIMATTER = 4
    STABLE = 5

for status in TypeStatus:
    print('{:15} = {:30}'.format(status.name, status.value))

class Molecule:
    """
    Represents a molecule composed of atoms.
    """
    def __init__(self, name, atoms):
        """
        Initialize a Molecule object.
        """
        self.name = name
        self.atoms = atoms

    def sort_atoms_by_mass(self):
        """
        Sort the atoms in the molecule based on their atomic masses.
        """
        self.atoms = sorted(self.atoms, key=lambda atom: atom.atomic_mass)
    
    def find_average_mass(self):
        """
        Calculate the average atomic mass of the atoms in the molecule.
        """
        if not self.atoms:
            return 0.0
        full_mass = sum(atom.atomic_mass for atom in self.atoms)
        average_mass = full_mass / len(self.atoms)
        return average_mass
    
if __name__ == "__main__":
    atom1 = Atom("Hydrogen", 1.008, 0, 1, 1)
    atom2 = Atom("Oxygen", 16.00, 8, 8, 8)
    atom3 = Atom("Carbon", 12.01, 6, 6, 6)
    
    molecule = Molecule("EveryAtom", [atom1, atom2, atom3])
    molecule.sort_atoms_by_mass()
    for atom in molecule.atoms:
        print(f"{atom.name}: {atom.atomic_mass} а.о.м.")
    
    for atom in [atom1, atom2, atom3]:
         print(f"Is neutral: {atom.isNeutral()}\n")

    average_mass = molecule.find_average_mass()
    print(f"the average mass of atoms in {molecule.name}: {average_mass} а.о.м.")     
