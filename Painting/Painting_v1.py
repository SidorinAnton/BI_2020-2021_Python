# Not finished version of painting

# TODO
# 1) Warp in functions
# 2) Usage from command line
# 3) Current programme needs a lot of memory :(
# 4) Try seaborn, plotly and bokeh for visualisation
# 5) Use another format of data (fasta), not only fastq
# 6) Add data name to names of paintings (??)

import numpy as np
import time
import argparse
import os
import matplotlib.pyplot as plt
import seaborn as sns


from statistics_of_reads_file import StatisticsOfReadsFile



# 1. Per base sequence quality
# 2. Per sequence quality scores
# 3. Per base sequence content
# 4. Per sequence GC content
# 5. Per base N content
# 6. Sequence Length Distribution

# Arguments:
#

parser = argparse.ArgumentParser()
parser.parse_args()


start_time = time.time()
fastq_statistic_values = StatisticsOfReadsFile()

path_to_input_file = "./Test_reads_cut.fastq"
fastq_statistic_values.parse_fastq_file(path_to_input_file)

print(fastq_statistic_values.get_coordinates_of_sequence_length_distribution())
exit()
# ______________ Directory for paintings ______________

path_to_save_paintings = "./Matplotlib_paintings"

if not os.path.exists(path_to_save_paintings):
    os.mkdir(path_to_save_paintings)
    print(f"Creating {path_to_save_paintings}")


# ______________ PLOTS ______________

# 1. Per base sequence quality
fig, ax = plt.subplots(figsize=(20, 10))

bp = ax.boxplot(read_quality_per_base_cut, positions=xval_per_base_seq_qual, patch_artist=True,
                widths=0.7, showfliers=False, labels=xlab_per_base_seq_qual)

ax.plot(xval_per_base_seq_qual, read_quality_per_base_mean, "b-")

fig.autofmt_xdate()

for patch in bp['boxes']:
    patch.set(facecolor="yellow")
    patch.set(alpha=0.7)

start, end = ax.get_ylim()
ax.yaxis.set_ticks(np.arange(int(0), int(end), 2))

ax.fill_between(xval_per_base_seq_qual, 0, 20, alpha=0.5, color="lightcoral")
ax.fill_between(xval_per_base_seq_qual, 20, 28, color="lightyellow")
ax.fill_between(xval_per_base_seq_qual, 28, 40, alpha=0.5, color="lightgreen")


plt.xlabel("Position in read (bp)")
plt.ylabel("Quality (Phred Score)")
plt.title("Quality scores across all bases")
plt.grid(axis="y")

plt.savefig(path_to_save_paintings + "/1_Per_base_sequence_quality.jpg", format="jpg", bb_inches="tight")
plt.close()

#
#

# 2. Per sequence quality scores
plt.figure(figsize=(20, 10))
plt.plot(x_per_seq_qual_scores, y_per_seq_qual_scores, color="red")
plt.xlabel("Mean Sequence Quality (Phred Score)")
plt.ylabel("Number of Sequence")
plt.title("Quality score distribution over all sequences")
plt.grid(axis="y")

plt.savefig(path_to_save_paintings + "/2_Per_sequence_quality_scores.jpg", format="jpg", bb_inches="tight")
plt.close()

#
#

# 3. Per base sequence content
fig, ax = plt.subplots(figsize=(20, 10))

ax.plot(xval_per_base_seq_and_N_content, T_per_base, color="red")
ax.plot(xval_per_base_seq_and_N_content, C_per_base, color="blue")
ax.plot(xval_per_base_seq_and_N_content, A_per_base, color="green")
ax.plot(xval_per_base_seq_and_N_content, G_per_base, color="black")

plt.xlabel("Position in read (bp)")
plt.gca().set_ylim([0, 100])
plt.title("Sequence content across all bases")
plt.grid(axis="y")
fig.autofmt_xdate()
plt.legend(("%T", "%C", "%A", "%G"), loc="upper right")

plt.savefig(path_to_save_paintings + "/3_Per_base_sequence_content.jpg", format="jpg", bb_inches="tight")
plt.close()

#
#

# 4. Per sequence GC content
plt.figure(figsize=(20, 10))
plt.plot(x_GC, y_GC, color="red")
plt.xlabel("Mean GC content (%)")
plt.ylabel("Number of Sequence")
plt.title("GC content distribution over all sequences")
plt.grid(axis="y")

plt.savefig(path_to_save_paintings + "/4_Per_sequence_GC_content.jpg", format="jpg", bb_inches="tight")
plt.close()

#
#

# 5. Per base N content
fig, ax = plt.subplots(figsize=(20, 10))
ax.plot(xval_per_base_seq_and_N_content, N_per_base, color="red")

plt.xlabel("Position in read (bp)")
plt.gca().set_ylim([0, 100])
plt.title("N content across all bases")
plt.grid(axis="y")
fig.autofmt_xdate()

plt.savefig(path_to_save_paintings + "/5_Per_base_N_content.jpg", format="jpg", bb_inches="tight")
plt.close()

#
#

# 6. Sequence Length Distribution
plt.figure(figsize=(20, 10))
plt.plot(x_len, y_len, color="red")

plt.xlabel("Sequence Length (bp)")
plt.ylabel("Number of Sequence")
plt.title("Sequence Length Distribution")
plt.grid(axis="y")

plt.savefig(path_to_save_paintings + "/6_Sequence_Length_Distribution.jpg", format="jpg", bb_inches="tight")
plt.close()

#
#

print()
print("Painting with Matplotlib is done")
print(f"Paintings were placed in {os.getcwd() + path_to_save_paintings[1:]}")



end_time = time.time()
print()
print("Running time", round(end_time - start_time, 3), "seconds")
