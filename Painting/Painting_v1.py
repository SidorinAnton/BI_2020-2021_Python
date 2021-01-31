
import numpy as np
import time
import argparse
import os
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings("ignore")

from statistics_of_reads_file import StatisticsOfReadsFile

# 1. Per base sequence quality
# 2. Per sequence quality scores
# 3. Per base sequence content
# 4. Per sequence GC content
# 5. Per base N content
# 6. Sequence Length Distribution

start_time = time.time()

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", type=str, help="path to fasta / fastq file")

parser.add_argument("-o", "--output_dir", type=str,
                    help="""path to dir where to store images. If this option is not set then the
                    output file for each sequence file is created in the same
                    directory as the sequence file which was processed.""")

args = parser.parse_args()

path_to_input_files = args.file
path_to_save_paintings = args.output_dir

# ______________ Directory for paintings ______________

if path_to_input_files is None:
    print("Input '.fastq' or '.fasta' or '.fna' file is not defined.")
    exit()

if path_to_save_paintings is None:
    path_to_save_paintings = "./Result_paintings"
# TODO - Check that path_to_output_dir is a dir
else:
    if path_to_save_paintings.endswith("/"):
        path_to_save_paintings = path_to_save_paintings[:-1]  # Delete the last "/"

if not os.path.exists(path_to_save_paintings):
    os.mkdir(path_to_save_paintings)
    print(f"Creating {path_to_save_paintings}")


print(f"""
Current parameters are:
- Input file with reads - {path_to_input_files},
- Path to save images - {path_to_save_paintings}
""", end="\n\n")


# ______________ PLOTS ______________

if path_to_input_files.endswith(".fastq"):
    fastq_statistic_values = StatisticsOfReadsFile()
    fastq_statistic_values.parse_fastq_file(path_to_input_files)


    # 1. Per base sequence quality
    fig, ax = plt.subplots(figsize=(20, 10))
    coordinates = fastq_statistic_values.get_coordinates_of_per_base_sequence_quality()

    bp = ax.boxplot(coordinates["y_val_boxplots"], positions=coordinates["values_of_x"], patch_artist=True,
                    widths=0.7, showfliers=False, labels=coordinates["labels_of_x"])

    ax.plot(coordinates["values_of_x"], coordinates["y_val_mean"], "b-")

    fig.autofmt_xdate()

    for patch in bp['boxes']:
        patch.set(facecolor="yellow")
        patch.set(alpha=0.7)

    start, end = ax.get_ylim()
    ax.yaxis.set_ticks(np.arange(int(0), int(end), 2))

    ax.fill_between(coordinates["values_of_x"], 0, 20, alpha=0.5, color="lightcoral")
    ax.fill_between(coordinates["values_of_x"], 20, 28, color="lightyellow")
    ax.fill_between(coordinates["values_of_x"], 28, 40, alpha=0.5, color="lightgreen")


    plt.xlabel("Position in read (bp)")
    plt.ylabel("Quality (Phred Score)")
    plt.title("Quality scores across all bases")
    plt.grid(axis="y")

    plt.savefig(path_to_save_paintings + "/PLT_1_Per_base_sequence_quality.jpg", format="jpg", bb_inches="tight")
    plt.close()

    #
    #

    # 2. Per sequence quality scores
    coordinates = fastq_statistic_values.get_coordinates_of_per_sequence_quality_scores()

    plt.figure(figsize=(20, 10))
    plt.plot(coordinates["values_of_x"], coordinates["values_of_y"], color="red")
    plt.xlabel("Mean Sequence Quality (Phred Score)")
    plt.ylabel("Number of Sequence")
    plt.title("Quality score distribution over all sequences")
    plt.grid(axis="y")

    plt.savefig(path_to_save_paintings + "/PLT_2_Per_sequence_quality_scores.jpg", format="jpg", bb_inches="tight")
    plt.close()

    #
    #

    # 3. Per base sequence content
    fig, ax = plt.subplots(figsize=(20, 10))
    coordinates = fastq_statistic_values.get_coordinates_of_per_base_sequence_content()

    ax.plot(coordinates["values_of_x"], coordinates["values_of_y_T"], color="red")
    ax.plot(coordinates["values_of_x"], coordinates["values_of_y_C"], color="blue")
    ax.plot(coordinates["values_of_x"], coordinates["values_of_y_A"], color="green")
    ax.plot(coordinates["values_of_x"], coordinates["values_of_y_G"], color="black")

    plt.xlabel("Position in read (bp)")
    plt.gca().set_ylim([0, 100])
    plt.title("Sequence content across all bases")
    plt.grid(axis="y")
    fig.autofmt_xdate()
    plt.legend(("%T", "%C", "%A", "%G"), loc="upper right")

    plt.savefig(path_to_save_paintings + "/PLT_3_Per_base_sequence_content.jpg", format="jpg", bb_inches="tight")
    plt.close()

    #
    #

    # 4. Per sequence GC content
    coordinates = fastq_statistic_values.get_coordinates_of_per_sequence_GC_content()

    plt.figure(figsize=(20, 10))
    plt.plot(coordinates["values_of_x"], coordinates["values_of_y"], color="red")
    plt.xlabel("Mean GC content (%)")
    plt.ylabel("Number of Sequence")
    plt.title("GC content distribution over all sequences")
    plt.grid(axis="y")

    plt.savefig(path_to_save_paintings + "/PLT_4_Per_sequence_GC_content.jpg", format="jpg", bb_inches="tight")
    plt.close()

    #
    #

    # 5. Per base N content
    fig, ax = plt.subplots(figsize=(20, 10))
    coordinates = fastq_statistic_values.get_coordinates_of_per_base_N_content()

    ax.plot(coordinates["values_of_x"], coordinates["values_of_y"], color="red")

    plt.xlabel("Position in read (bp)")
    plt.gca().set_ylim([0, 100])
    plt.title("N content across all bases")
    plt.grid(axis="y")
    fig.autofmt_xdate()

    plt.savefig(path_to_save_paintings + "/PLT_5_Per_base_N_content.jpg", format="jpg", bb_inches="tight")
    plt.close()

    #
    #

    # 6. Sequence Length Distribution
    coordinates = fastq_statistic_values.get_coordinates_of_sequence_length_distribution()

    plt.figure(figsize=(20, 10))
    plt.plot(coordinates["values_of_x"], coordinates["values_of_y"], color="red")

    plt.xlabel("Sequence Length (bp)")
    plt.ylabel("Number of Sequence")
    plt.title("Sequence Length Distribution")
    plt.grid(axis="y")

    plt.savefig(path_to_save_paintings + "/PLT_6_Sequence_Length_Distribution.jpg", format="jpg", bb_inches="tight")
    plt.close()

    #
    #

elif path_to_input_files.endswith(".fasta") or path_to_input_files.endswith(".fna"):
    fasta_statistic_values = StatisticsOfReadsFile()
    fasta_statistic_values.parse_fasta_file(path_to_input_files)

    # Sequence Length Distribution
    coordinates = fasta_statistic_values.get_coordinates_of_sequence_length_distribution()

    plt.figure(figsize=(20, 10))
    plt.plot(coordinates["values_of_x"], coordinates["values_of_y"], color="red")

    plt.xlabel("Sequence Length (bp)")
    plt.ylabel("Number of Sequence")
    plt.title("Sequence Length Distribution")
    plt.grid(axis="y")

    plt.savefig(path_to_save_paintings + "/PLT_6_Sequence_Length_Distribution.jpg", format="jpg", bb_inches="tight")
    plt.close()

else:  # not a fasta / fastq format in file name
    print(f"File {path_to_input_files} didn't exist, or couldn't be read")
    exit()

print()
print("Painting with Matplotlib is done")
print(f"Paintings were placed in {path_to_save_paintings}")


end_time = time.time()
print()
print("Running time", round(end_time - start_time, 3), "seconds")
