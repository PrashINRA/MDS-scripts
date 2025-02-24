#!/bin/bash
#SBATCH --job-name=cellranger_multi_counts    # Job name
#SBATCH --output=cellranger_multi_counts.out  # Standard output log
#SBATCH --error=cellranger_multi_counts.err   # Standard error log
#SBATCH --time=48:00:00                       # Time limit (hh:mm:ss)
#SBATCH --mem=100G                            # Memory allocation
#SBATCH --partition=defq                      # Partition name
#SBATCH --cpus-per-task=16                    # Number of CPU cores
#SBATCH --mail-type=END,FAIL                  # Email notifications
#SBATCH --mail-user=m.afechkar@amsterdamumc.nl # Your email for notifications

# ------------------------------
# Cell Ranger Multi: Generate Count Matrices
# This script uses multi_config.csv to process both GEX and Protein data.
# ------------------------------

# Set the working directory and file paths
WORKDIR="/net/beegfs/scratch/mafechkar/MDA_Data"
cd "$WORKDIR" || { echo "ERROR: Cannot access $WORKDIR"; exit 1; }

# Define paths to configuration file and output directory
CONFIG_FILE="$WORKDIR/metadata/multi_config.csv"
OUTPUT_DIR="$WORKDIR/MDS_Output"

# Check if multi_config.csv exists
if [ ! -f "$CONFIG_FILE" ]; then
    echo "ERROR: Configuration file not found: $CONFIG_FILE"
    exit 1
fi

# Create the output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Optionally, load the cellranger module if needed on your system
module load cellranger 2>/dev/null

# Run Cell Ranger Multi using the configuration file
echo "Starting Cell Ranger Multi at $(date)..."
cellranger multi --id=MDS_Output --csv="$CONFIG_FILE" --localcores=16 --localmem=100 2>&1 | tee "$OUTPUT_DIR/cellranger_multi.log"

# Check if the command ran successfully
if [ $? -eq 0 ]; then
    echo "Cell Ranger Multi completed successfully at $(date)."
    echo "Output is in: $OUTPUT_DIR"
else
    echo "Cell Ranger Multi encountered an error. Check the log file at: $OUTPUT_DIR/cellranger_multi.log"
    exit 1
fi

echo "Job complete!"
