import pandas as pd

antibody_file = "/net/beegfs/scratch/mafechkar/MDS_Data/metadata/Kopie von TotalSeq_C_Human_Universal_Cocktail_v1_137_Antibodies_399905_Barcodes.xlsx"
df = pd.read_excel(antibody_file, engine='openpyxl')

probe_set_df = pd.DataFrame({
    "gene_id": df["Ensemble ID"],  
    "probe_id": df["DNA_ID"],
    "probe_seq": df["Barcode"]
})

probe_set_output = "/net/beegfs/scratch/mafechkar/MDS_Data/metadata/probe_set.csv"

with open(output_csv, "w") as f:
    f.write("#panel_name=TotalSeq_C_Human_Universal\n")
    f.write("#panel_type=CITE-seq\n")
    f.write("#reference_genome=GRCh38\n")
    f.write("#reference_version=1.0.0\n")
    f.write("#probe_set_file_format=10x_v1\n")
    probe_set_df.to_csv(f, index=False)
    
print(f"Probe set CSV file has been created at {probe_set_output}")


