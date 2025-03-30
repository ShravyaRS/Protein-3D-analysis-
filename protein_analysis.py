from Bio import PDB
import requests
import py3Dmol

# Function to download PDB file
def download_pdb(protein_id):
    url = f"https://files.rcsb.org/download/{protein_id}.pdb"
    response = requests.get(url)
    if response.status_code == 200:
        with open(f"{protein_id}.pdb", "wb") as file:
            file.write(response.content)
        print(f"✅ Downloaded {protein_id}.pdb successfully!")
    else:
        print("❌ Error: Unable to download PDB file.")

# Function to parse PDB structure
def parse_pdb(protein_id):
    parser = PDB.PDBParser(QUIET=True)
    structure = parser.get_structure(protein_id, f"{protein_id}.pdb")
    print(f"✅ Parsed structure: {protein_id}")
    return structure

# Function to calculate molecular weight
def calculate_molecular_weight(structure):
    weight = sum(atom.element.mass for model in structure for chain in model for residue in chain for atom in residue)
    print(f"⚖ Molecular Weight: {weight:.2f} Da")
    return weight

# Function to visualize 3D structure
def visualize_protein(protein_id):
    viewer = py3Dmol.view(query=f"pdb:{protein_id}")
    viewer.setStyle({'cartoon': {'color': 'spectrum'}})
    viewer.show()

# Example Protein ID (Hemoglobin - 1HHO)
protein_id = "1HHO"
download_pdb(protein_id)
structure = parse_pdb(protein_id)
calculate_molecular_weight(structure)
visualize_protein(protein_id)
