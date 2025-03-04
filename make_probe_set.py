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


t Tue Mar  4 14:33:59 CET 2025...


Martian Runtime - v4.0.13
2025-03-04 14:34:00 [jobmngr] WARNING: User-supplied amount 300 GB is higher than the detected cgroup memory limit of 40.0 GB
Serving UI at http://node010.cluster:36535?auth=jOfm5QhPllTiquEoxyEE50yueVrbTe4mLrx1Y8iNFwM

Running preflight checks (please wait)...

[error] Pipestance failed. Error log at:
MDS_Output/SC_MULTI_CS/MULTI_PREFLIGHT/fork0/chnk0-u2462c70148/_errors

Log message:
The following metadata fields are required in the probe set CSV header: "panel_name", "panel_type", "reference_genome", "reference_version", but were not found. Please include these fields in #field=value format at the top of the file.

Waiting 6 seconds for UI to do final refresh.
Pipestance failed. Use --noexit option to keep UI running after failure.

2025-03-04 14:34:24 Shutting down.
Saving pipestance info to "MDS_Output/MDS_Output.mri.tgz"
For assistance, upload this file to 10x Genomics by running:

cellranger upload <your_email> "MDS_Output/MDS_Output.mri.tgz"

Cell Ranger Multi finished at Tue Mar  4 14:34:24 CET 2025. Output is in: /net/beegfs/scratch/mafechkar/MDS_Data/MDS_Output
[mafechkar@ares mafechkar]$
