import pandas as pd
antibody_file = "/net/beegfs/scratch/mafechkar/MDS_Data/metadata/Kopie van TotalSeq_C_Human_Universal_Cocktail_v1_137_Antibodies_399905_Barcodes.xlsx"

df = pd.read_excel(antibody_file, engine='openpyxl')

probe_set_df = pd.DataFrame({
    "gene_id": df["Ensemble ID"],
    "probe_seq": df["Barcode"],
    "probe_id": df["DNA_ID"]
})

output_probe_csv = "/net/beegfs/scratch/mafechkar/MDS_Data/metadata/probe_set.csv"

with open(output_probe_csv, "w") as f:
    f.write("#panel_name=TotalSeq_C_Human_Universal\n")
    f.write("#panel_type=CITE-seq\n")
    f.write("#reference_genome=GRCh38\n")
    f.write("#reference_version=2020-A\n")
    f.write("#probe_set_file_format=10x_v1\n")
    probe_set_df.to_csv(f, index=False)

print(f"Probe set CSV file has been created at {output_probe_csv}")

///

 cat cellranger_multi_counts.out
Starting Cell Ranger Multi at Tue Mar  4 15:20:30 CET 2025...


Martian Runtime - v4.0.13
2025-03-04 15:20:30 [jobmngr] WARNING: User-supplied amount 300 GB is higher than the detected cgroup memory limit of 40.0 GB
Serving UI at http://node001.cluster:36595?auth=TZp9aw8yyH2NL47iDslg9n-w2jN_jrcADQWZReGro60

Running preflight checks (please wait)...

[error] Pipestance failed. Error log at:
MDS_Output/SC_MULTI_CS/MULTI_PREFLIGHT/fork0/chnk0-u7593c70c2e/_errors

Log message:
The feature reference file header does not contain one or more required comma-separated fields: "id, name, read, pattern, sequence, feature_type".
The following fields were found: "".
Please check that your file is in CSV format and has the required field names.

Waiting 6 seconds for UI to do final refresh.
Pipestance failed. Use --noexit option to keep UI running after failure.

2025-03-04 15:20:45 Shutting down.
Saving pipestance info to "MDS_Output/MDS_Output.mri.tgz"
For assistance, upload this file to 10x Genomics by running:

cellranger upload <your_email> "MDS_Output/MDS_Output.mri.tgz"

Cell Ranger Multi finished at Tue Mar  4 15:20:46 CET 2025. Output is in: /net/beegfs/scratch/mafechkar/MDS_Data/MDS_Output


