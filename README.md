mkdir -p /net/beegfs/scratch/mafechkar/MDA_Data/metadata


nano /net/beegfs/scratch/mafechkar/MDS_Data/split_metadata.py
#!/usr/bin/env python3
import pandas as pd

# Path to your Excel file (adjust if necessary)
metadata_file = "/net/beegfs/scratch/mafechkar/MDS_Data/Data for scRNA seq analysis Updated.xlsx"

# Read the Excel file:
# header=1 means the second row is used as the header,
# sheet_name=1 uses the second sheet.
metadata = pd.read_excel(metadata_file, engine='openpyxl', header=1, sheet_name=1)

# For GEX: extract the columns "MDS#" and "Index for GEX library"
# and rename them to "Sample" and "Index" respectively.
gex_samples = metadata[['MDS#', 'Index for GEX library']].copy()
gex_samples.rename(columns={'MDS#': 'Sample', 'Index for GEX library': 'Index'}, inplace=True)
# Add a Lane column with a default value (e.g., "*")
gex_samples.insert(0, 'Lane', '*')
# Optionally, append a suffix to sample names to indicate modality
gex_samples['Sample'] = gex_samples['Sample'].astype(str) + "_GEX"

# For Protein: extract the columns "MDS#" and "Index ab (Protein) library"
protein_samples = metadata[['MDS#', 'Index ab (Protein) library']].copy()
protein_samples.rename(columns={'MDS#': 'Sample', 'Index ab (Protein) library': 'Index'}, inplace=True)
protein_samples.insert(0, 'Lane', '*')
protein_samples['Sample'] = protein_samples['Sample'].astype(str) + "_PROT"

# Save the two sample sheets as CSV files in your working directory on the cluster.
gex_samples.to_csv('/net/beegfs/scratch/mafechkar/gex_samples.csv', index=False)
protein_samples.to_csv('/net/beegfs/scratch/mafechkar/protein_samples.csv', index=False)

print("Successfully split metadata into gex_samples.csv and protein_samples.csv")


python3 /net/beegfs/scratch/mafechkar/split_metadata.py
ls -lh /net/beegfs/scratch/mafechkar/gex_samples.csv
ls -lh /net/beegfs/scratch/mafechkar/protein_samples.csv
head /net/beegfs/scratch/mafechkar/gex_samples.csv
head /net/beegfs/scratch/mafechkar/protein_samples.csv


