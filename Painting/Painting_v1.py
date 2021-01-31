# Not finished version of painting

# TODO
# 1) Warp in functions
# 2) Usage from command line
# 3) Current programme needs a lot of memory :(
# 4) Try seaborn, plotly and bokeh for visualisation
# 5) Use another format of data (fasta), not only fastq
# 6) Add data name to names of paintings (??)

from collections import Counter
import statistics as stat
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
import time


start_time = time.time()
# 1. Per base sequence quality
# 2. Per sequence quality scores
# 3. Per base sequence content
# 4. Per sequence GC content
# 5. Per base N content
# 6. Sequence Length Distribution

# I use list comprehension [[] for _ in range(1000)] to make a structure, where
# indexes of outer list are the position in reads (sequence itself or it's quality).
# So [0] element of this list - nucleotid (or it's quality) in the first position of every read.
# That is why I use in range(1000). I suggest that length of reads from Illumina couldn't be greater than 400.


read_quality_per_base = [[] for _ in range(1000)]  # 1. Per base sequence quality
read_quality_per_base_mean = []  # 1. Per base sequence quality

read_quality_per_seq = []  # 2. Per sequence quality scores

sequence_content = [[] for _ in range(1000)]  # 3. Per base sequence content and 5. Per base N content
A_per_base = []  # 3. Per base sequence content
T_per_base = []  # 3. Per base sequence content
G_per_base = []  # 3. Per base sequence content
C_per_base = []  # 3. Per base sequence content
GC_content = []  # 4. Per sequence GC content
N_per_base = []  # 5. Per base N content
read_len = []  # 6. Sequence Length Distribution

# with open("Raddei.fastq", "r") as fastq_data:  # 5.6 Gb of data. Not working !!!
with open("Test_reads_full.fastq", "r") as fastq_data:  # Full
# with open("Test_reads_cut.fastq", "r") as fastq_data:  # Cut (Len of reads < 50 p.b.)
    print("Start reading")
    short_data_counter = 0  # For testing

    line_number = 0
    for line in fastq_data:
        # Usually read in fastq format takes 4 lines (Name, sequence, comment and quality)

        short_data_counter += 1  # For testing
        line_number += 1

        # line_number == 1 - Name and technical information of read

        if line_number == 2:  # String with nucleotides

            # Count GC (4. Per sequence GC content)
            # Here we make a list with GC% from the every read (sequence)
            GC = 100 * ((line.rstrip().count("G")) + (line.rstrip().count("C"))) / len(line.rstrip())
            GC_content.append(int(GC))  # [44, 43, 45, 44]

            # For T, G, C, A and N content (3. Per base sequence content and 5. Per base N content)
            # Here we make an array (list of lists), where index of each list presents the position in read (sequence).
            # Based on this structure we will draw the distribution of every nucleotide (and N).
            for i in range(len(line.rstrip())):
                sequence_content[i].append(line.rstrip()[i])  # [['T', 'N', 'G', 'G'], [...], ...]

            # For len distribution (6. Sequence Length Distribution)
            # Make a list with length of each read (sequence)
            read_len.append(len(line.rstrip()))  # [149, 151, 123, 108]

        # line_number == 3  - Comment string, start's with "+"

        elif line_number == 4:  # String with quality

            # Get quality (Phred Score)
            phred_value = [ord(ch) - 33 for ch in line.rstrip()]  # Convert from ASCII format

            # For "1. Per base sequence quality"
            # Make an array (list of lists), where index of outer list - position in read.
            for i in range(len(phred_value)):
                read_quality_per_base[i].append(phred_value[i])  # [[11, 24, 30, 34], [...], [...], ...]

            # For "2. Per sequence quality scores"
            # And here make a list with mean quality per every read.
            read_quality_per_seq.append(int(stat.mean(phred_value)))  # [30, 37, 22, 36]

            line_number = 0  # Start again

        # _______ For testing _______
        # if short_data_counter > 16:
        #     break

print("Reading data is done")
print()

# ______________ Preprocessing ______________
print("Start processing the data")
# 1. Per base sequence quality
'''
Names for painting:
    xlab_per_base_seq_qual - name of each x value
    xval_per_base_seq_qual - x value
    read_quality_per_base_cut - y values for boxplots (for each x value)
    read_quality_per_base_mean - y values for mean (for each x value)
'''

# Drop the empty lists (Thus, length of read_quality_per_base == length of the longest read)
read_quality_per_base = read_quality_per_base[:read_quality_per_base.index([])]

# To visualize. If there are reads with length > 50,
# we will make a step. First 10 positions, and then make a window of 5 (10-14, 15-19, ...)
if len(read_quality_per_base) > 50:
    read_quality_per_base_cut = read_quality_per_base[:9]
    xlab_per_base_seq_qual = [str(i) for i in range(1, 10)]  # labels of OX scale (in "Per base sequence quality")

    for i in range(15, len(read_quality_per_base), 5):
        sub_list = []
        for sub in read_quality_per_base[i - 5:i - 1]:
            for item in sub:
                sub_list.append(item)

        read_quality_per_base_cut.append(sub_list)
        xlab_per_base_seq_qual.append(f"{i - 5}-{i - 1}")

else:
    read_quality_per_base_cut = read_quality_per_base[:]
    xlab_per_base_seq_qual = [str(i) for i in range(1, len(read_quality_per_base) + 1)]


# For mean quality. It is necessary to draw the line in "Per base sequence quality"
for val_list in read_quality_per_base_cut:
    read_quality_per_base_mean.append(int(stat.mean(val_list)))

xval_per_base_seq_qual = [i for i in range(len(xlab_per_base_seq_qual))]  # values of OX scale (in "Per base sequence quality")

#
#

# 2. Per sequence quality scores
sorted_quality_data = sorted(read_quality_per_seq)  # Sort the values of mean quality of reads
count_quality = Counter(sorted_quality_data)  # And count every value

x_per_seq_qual_scores = list(count_quality.keys())  # x value in "Per sequence quality scores"
y_per_seq_qual_scores = list(count_quality.values())  # y value in "Per sequence quality scores"

#
#

# 3. Per base sequence content and 5. Per base N content
# The same idea as in the 1.
# Drop the empty lists (Thus, length of sequence_content == length of the longest read)
sequence_content = sequence_content[:sequence_content.index([])]

# To visualize. If there are reads with length > 50,
# we will make a step. First 20 positions, and then make a window of 5 (20-24, 25-29, ...)
if len(sequence_content) > 50:
    sequence_content_cut = sequence_content[:19]
    xval_per_base_seq_and_N_content = [str(i) for i in range(1, 20)]

    for i in range(25, len(sequence_content), 5):
        sub_list = []
        for sub in sequence_content[i - 5:i - 1]:
            for item in sub:
                sub_list.append(item)

        sequence_content_cut.append(sub_list)
        xval_per_base_seq_and_N_content.append(f"{i - 5}-{i - 1}")

else:
    sequence_content_cut = sequence_content[:]
    xval_per_base_seq_and_N_content = [str(i) for i in range(1, len(sequence_content) + 1)]


for content_per_base in sequence_content_cut:
    A_val = 100 * (content_per_base.count("A") / len(content_per_base))
    T_val = 100 * (content_per_base.count("T") / len(content_per_base))
    G_val = 100 * (content_per_base.count("G") / len(content_per_base))
    C_val = 100 * (content_per_base.count("C") / len(content_per_base))
    N_val = 100 * (content_per_base.count("N") / len(content_per_base))

    A_per_base.append(A_val)  # y value
    T_per_base.append(T_val)  # y value
    G_per_base.append(G_val)  # y value
    C_per_base.append(C_val)  # y value
    N_per_base.append(N_val)  # y value

    # xval_per_base_seq_and_N_content - x value

#
#

# 4. Per sequence GC content
GC_content = sorted(GC_content)  # Sort the values of GC content of reads
count_GC_content = Counter(GC_content)  # And count every value

x_GC = list(count_GC_content.keys())  # x value
y_GC = list(count_GC_content.values())  # y value

#
#

# 6. Sequence Length Distribution
sorted_len_data = sorted(read_len)  # Sort the values of leangth of reads
count_len = Counter(sorted_len_data)  # And count every value
# count = {i: len_data.count(i) for i in len_data_sort}  # Much slower than collections.Counter

x_len = list(count_len.keys())  # x value
y_len = list(count_len.values())  # y value

print("Preprocessing is done")




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
