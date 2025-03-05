import pandas as pd

antibody_file = "/net/beegfs/scratch/mafechkar/MDS_Data/metadata/Kopie van TotalSeq_C_Human_Universal_Cocktail_v1_137_Antibodies_399905_Barcodes.xlsx"

df = pd.read_excel(antibody_file, engine='openpyxl')

# Create the feature reference DataFrame with the required columns and order:
feature_df = pd.DataFrame({
    "id": df["DNA_ID"],                 
    "name": df["Gene name"],              
    "read": "AntibodyCapture",           
    "pattern": "",                       
    "sequence": df["Barcode"],           
    "feature_type": "Antibody Capture"   
})

output_csv = "/net/beegfs/scratch/mafechkar/MDS_Data/metadata/feature_ref.csv"

# Opening the output file and writing the metadata header lines, then append the DataFrame
with open(output_csv, "w") as f:
    f.write("#panel_name=TotalSeq_C_Human_Universal\n")
    f.write("#panel_type=CITE-seq\n")
    f.write("#reference_genome=GRCh38\n")
    f.write("#reference_version=2020-A\n")
    f.write("#probe_set_file_format=10x_v1\n")
    feature_df.to_csv(f, index=False)

print(f"Feature reference CSV file has been created at {output_csv}")

python3 make_feature_ref.py



