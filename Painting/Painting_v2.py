
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

import time

# # Structure
# 1) Function to read data into two tables (table with sequences and table with it's quality).
#       Columns of these tables - position in read, rows (indexes) - number of read.

# TODO
# index of rows - first line (name of read)
# may be create a tmp files and then read them ?
# or create a tmp df when number of roads > 1000 ?

# 2) Function to make paintings using matplotlib
# 3) Function to make paintings using seaborn


columns = [i for i in range(1, 1000)]  # Length of reads from Illumina must be < 1000

reads_sequence_data = pd.DataFrame(columns=columns)
quality_data = pd.DataFrame(columns=columns)
tmp_reads_seq_data = pd.DataFrame(columns=columns)
tmp_quality_data = pd.DataFrame(columns=columns)

start_time = time.time()

# with open("Raddei.fastq", "r") as fastq_data:  # 5.6 Gb of data !!! Very slow !!!
with open("Test_reads_full.fastq", "r") as fastq_data:  # Full
# with open("Test_reads_cut.fastq", "r") as fastq_data:  # Cut (Len of reads < 50 p.b.)

    line_number = 0

    for line in fastq_data:
        line_number += 1

        if line_number == 2:  # String with read sequence

            read = list(line.rstrip())

            read_sequence_row = pd.DataFrame(data=[read])
            tmp_reads_seq_data = tmp_reads_seq_data.append(read_sequence_row, ignore_index=True)

            # tmp_reads_seq_data = tmp_reads_seq_data.append([list(line.rstrip())], ignore_index=True)

        elif line_number == 4:  # String with quality

            phred_value = [ord(ch) - 33 for ch in line.rstrip()]  # Calculate Phred score
            # phred_value = list(line.rstrip())  # May be calculate Phred score later ?

            quality_row = pd.DataFrame(data=[phred_value])
            tmp_quality_data = tmp_quality_data.append(quality_row, ignore_index=True)

            # tmp_quality_data = tmp_quality_data.append([list(line.rstrip())], ignore_index=True)

            line_number = 0

            print(tmp_reads_seq_data.shape, tmp_quality_data.shape)
            # break

        if tmp_quality_data.shape[0] == 500:
            reads_sequence_data = reads_sequence_data.append(tmp_reads_seq_data, ignore_index=True)
            quality_data = quality_data.append(tmp_quality_data, ignore_index=True)
            tmp_reads_seq_data = pd.DataFrame(columns=columns)
            tmp_quality_data = pd.DataFrame(columns=columns)


end_time = time.time()
print()
print("Running time", round(end_time - start_time, 3))

reads_sequence_data = reads_sequence_data.append(tmp_reads_seq_data, ignore_index=True)
quality_data = quality_data.append(tmp_quality_data, ignore_index=True)

print()
print(reads_sequence_data.dropna(axis=1, how="all"))
print(quality_data.dropna(axis=1, how="all"))
#
# print()
# print(tmp_reads_seq_data.dropna(axis=1, how="all"))
# print(tmp_quality_data.dropna(axis=1, how="all"))

