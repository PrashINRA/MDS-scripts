import pandas as pd

antibody_file = "/net/beegfs/scratch/mafechkar/MDS_Data/metadata/Kopie von TotalSeq_C_Human_Universal_Cocktail_v1_137_Antibodies_399905_Barcodes.xlsx"
df = pd.read_excel(antibody_file, engine='openpyxl')

probe_set_df = pd.DataFrame({
    "gene_id": df["Ensemble ID"],  # or use df["Gene name"] if that's preferred
    "probe_id": df["DNA_ID"],
    "probe_seq": df["Barcode"]
})

probe_set_output = "/net/beegfs/scratch/mafechkar/MDS_Data/metadata/probe_set.csv"
probe_set_df.to_csv(probe_set_output, index=False)
print(f"Probe set CSV file has been created at {probe_set_output}")
