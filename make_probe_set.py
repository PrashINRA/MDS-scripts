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


Feature reference CSV file has been created at /net/beegfs/scratch/mafechkar/MDS_Data/metadata/feature_ref.csv
[mafechkar@ares mafechkar]$ python3 /net/beegfs/scratch/mafechkar/MDS_Data/metadata/make_probe_set.py
Traceback (most recent call last):
  File "/net/beegfs/scratch/mafechkar/MDS_Data/metadata/make_probe_set.py", line 4, in <module>
    df = pd.read_excel(antibody_file, engine='openpyxl')
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/trinity/home/mafechkar/miniconda3/lib/python3.12/site-packages/pandas/io/excel/_base.py", line 495, in read_excel
    io = ExcelFile(
         ^^^^^^^^^^
  File "/trinity/home/mafechkar/miniconda3/lib/python3.12/site-packages/pandas/io/excel/_base.py", line 1567, in __init__
    self._reader = self._engines[engine](
                   ^^^^^^^^^^^^^^^^^^^^^^
  File "/trinity/home/mafechkar/miniconda3/lib/python3.12/site-packages/pandas/io/excel/_openpyxl.py", line 553, in __init__
    super().__init__(
  File "/trinity/home/mafechkar/miniconda3/lib/python3.12/site-packages/pandas/io/excel/_base.py", line 563, in __init__
    self.handles = get_handle(
                   ^^^^^^^^^^^
  File "/trinity/home/mafechkar/miniconda3/lib/python3.12/site-packages/pandas/io/common.py", line 882, in get_handle
    handle = open(handle, ioargs.mode)
             ^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: '/net/beegfs/scratch/mafechkar/MDS_Data/metadata/Kopie von TotalSeq_C_Human_Universal_Cocktail_v1_137_Antibodies_399905_Barcodes.xlsx'
