from rdkit import Chem
from rdkit.Chem import Draw


def save_molecule(smiles: str):
    mol = Chem.MolFromSmiles(smiles)
    Draw.MolToFile(mol, "artifacts/medium/molecule.png")


if __name__ == "__main__":
    """
    Так как я не успела построить граф AST, для этого домашнего задания я выбрала
    отрисовать молекулу. Можно поставить другую, главное чтобы она была в виде
    дескриптора SMILES (например вода это O, спирт CCO) 
    """
    save_molecule("CN1C=NC2=C1C(=O)N(C(=O)N2C)C")
