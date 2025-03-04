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



head /net/beegfs/scratch/mafechkar/MDS_Data/metadata/feature_ref.csv
#panel_name=TotalSeq_C_Human_Universal
#panel_type=CITE-seq
#reference_genome=GRCh38
#reference_version=2020-A
#probe_set_file_format=10x_v1
id,name,read,pattern,sequence,feature_type
C0006,CD86,AntibodyCapture,,GTCTTTGTCAGTGCA,Antibody Capture
C0007,CD274,AntibodyCapture,,GTTGTCCGACAATAC,Antibody Capture
C0020,TNFRSF14,AntibodyCapture,,TGATAGAAACAGACC,Antibody Capture
C0023,PVR,AntibodyCapture,,ATCACATCGTTGCCA,Antibody Capture




