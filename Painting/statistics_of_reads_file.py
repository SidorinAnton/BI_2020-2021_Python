
# Make a Class to calculate statistics of fastq file.
# Then use these values in painting file

# I use list comprehension [[] for _ in range(1000)] to make a structure, where
# indexes of outer list are the position in reads (sequence itself or it's quality).
# So [0] element of this list - nucleotid (or it's quality) in the first position of every read.
# That is why I use in range(1000). I suggest that length of reads from Illumina couldn't be greater than 400.


class StatisticsOfReadsFile:
    """

    """
    def __init__(self):
        self.read_quality_per_base = [[] for _ in range(1000)]  # 1. Per base sequence quality
        self.read_quality_per_seq = []  # 2. Per sequence quality scores
        self.sequence_content = [[] for _ in range(1000)]  # 3. Per base sequence content and 5. Per base N content
        self.GC_content = []  # 4. Per sequence GC content
        self.read_len = []  # 6. Sequence Length Distribution

        # # Values that are required for painting:
        # 1. Per base sequence quality
        self.read_quality_per_base_cut = None  # OY values for boxplots (for each x value)
        self.xlab_per_base_seq_qual = None  # Name of each x value
        self.xval_per_base_seq_qual = None  # OX values
        self.read_quality_per_base_mean = []  # OY values for mean (for each x value)

        # 2. Per sequence quality scores
        self.x_per_seq_qual_scores = None  # x values
        self.y_per_seq_qual_scores = None  # y values

        # 3. Per base sequence content and  # 5. Per base N content
        self.xval_per_base_seq_and_N_content = None  # x values
        self.A_per_base = []  # y values
        self.T_per_base = []  # y values
        self.G_per_base = []  # y values
        self.C_per_base = []  # y values
        self.N_per_base = []  # y values

        # 4. Per sequence GC content
        self.x_GC = None  # x values
        self.y_GC = None  # y values

        # 6. Sequence Length Distribution
        self.x_len = None  # x values
        self.y_len = None  # y values

    def parse_fastq_file(self, path_to_input_file: str) -> None:

        """

        :param path_to_input_file:
        :return:
        """

        from collections import Counter
        import statistics as stat

        # ______________ Reading ______________

        with open(path_to_input_file, "r") as fastq_data:  # Full
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
                    self.GC = 100 * ((line.rstrip().count("G")) + (line.rstrip().count("C"))) / len(line.rstrip())
                    self.GC_content.append(int(self.GC))  # [44, 43, 45, 44]

                    # For T, G, C, A and N content (3. Per base sequence content and 5. Per base N content)
                    # Here we make an array (list of lists), where index of each list presents the position in read (sequence).
                    # Based on this structure we will draw the distribution of every nucleotide (and N).
                    for i in range(len(line.rstrip())):
                        self.sequence_content[i].append(line.rstrip()[i])  # [['T', 'N', 'G', 'G'], [...], ...]

                    # For len distribution (6. Sequence Length Distribution)
                    # Make a list with length of each read (sequence)
                    self.read_len.append(len(line.rstrip()))  # [149, 151, 123, 108]

                # line_number == 3  - Comment string, start's with "+"

                elif line_number == 4:  # String with quality

                    # Get quality (Phred Score)
                    phred_value = [ord(ch) - 33 for ch in line.rstrip()]  # Convert from ASCII format

                    # For "1. Per base sequence quality"
                    # Make an array (list of lists), where index of outer list - position in read.
                    for i in range(len(phred_value)):
                        self.read_quality_per_base[i].append(phred_value[i])  # [[11, 24, 30, 34], [...], ...]

                    # For "2. Per sequence quality scores"
                    # And here make a list with mean quality per every read.
                    self.read_quality_per_seq.append(int(stat.mean(phred_value)))  # [30, 37, 22, 36]

                    line_number = 0  # Start again

                # _______ For testing _______
                # if short_data_counter > 16:
                #     break

        print("Reading data is done")
        print()

        # ______________ Preprocessing ______________
        print("Start processing the data")
        # 1. Per base sequence quality

        # Drop the empty lists (Thus, length of read_quality_per_base == length of the longest read)
        self.read_quality_per_base = self.read_quality_per_base[:self.read_quality_per_base.index([])]

        # To visualize. If there are reads with length > 50,
        # we will make a step. First 10 positions, and then make a window of 5 (10-14, 15-19, ...)
        if len(self.read_quality_per_base) > 50:
            self.read_quality_per_base_cut = self.read_quality_per_base[:9]
            self.xlab_per_base_seq_qual = [str(i) for i in range(1, 10)]  # labels of OX scale (in "Per base sequence quality")

            for i in range(15, len(self.read_quality_per_base), 5):
                sub_list = []
                for sub in self.read_quality_per_base[i - 5:i - 1]:
                    for item in sub:
                        sub_list.append(item)

                self.read_quality_per_base_cut.append(sub_list)
                self.xlab_per_base_seq_qual.append(f"{i - 5}-{i - 1}")

        else:
            self.read_quality_per_base_cut = self.read_quality_per_base[:]
            self.xlab_per_base_seq_qual = [str(i) for i in range(1, len(self.read_quality_per_base) + 1)]

        # For mean quality. It is necessary to draw the line in "Per base sequence quality"
        for val_list in self.read_quality_per_base_cut:
            self.read_quality_per_base_mean.append(int(stat.mean(val_list)))

        self.xval_per_base_seq_qual = [i for i in range(len(self.xlab_per_base_seq_qual))]  # values of OX scale (in "Per base sequence quality")

        #
        #

        # 2. Per sequence quality scores
        count_quality = Counter(sorted(self.read_quality_per_seq))  # Count the values of mean quality of reads

        self.x_per_seq_qual_scores = list(count_quality.keys())  # x value in "Per sequence quality scores"
        self.y_per_seq_qual_scores = list(count_quality.values())  # y value in "Per sequence quality scores"

        #
        #

        # 3. Per base sequence content and 5. Per base N content
        # The same idea as in the 1.
        # Drop the empty lists (Thus, length of sequence_content == length of the longest read)
        self.sequence_content = self.sequence_content[:self.sequence_content.index([])]

        # To visualize. If there are reads with length > 50,
        # we will make a step. First 20 positions, and then make a window of 5 (20-24, 25-29, ...)
        if len(self.sequence_content) > 50:
            sequence_content_cut = self.sequence_content[:19]
            self.xval_per_base_seq_and_N_content = [str(i) for i in range(1, 20)]

            for i in range(25, len(self.sequence_content), 5):
                sub_list = []
                for sub in self.sequence_content[i - 5:i - 1]:
                    for item in sub:
                        sub_list.append(item)

                sequence_content_cut.append(sub_list)
                self.xval_per_base_seq_and_N_content.append(f"{i - 5}-{i - 1}")

        else:
            sequence_content_cut = self.sequence_content[:]
            self.xval_per_base_seq_and_N_content = [str(i) for i in range(1, len(self.sequence_content) + 1)]

        for content_per_base in sequence_content_cut:
            A_val = 100 * (content_per_base.count("A") / len(content_per_base))
            T_val = 100 * (content_per_base.count("T") / len(content_per_base))
            G_val = 100 * (content_per_base.count("G") / len(content_per_base))
            C_val = 100 * (content_per_base.count("C") / len(content_per_base))
            N_val = 100 * (content_per_base.count("N") / len(content_per_base))

            self.A_per_base.append(A_val)  # y value
            self.T_per_base.append(T_val)  # y value
            self.G_per_base.append(G_val)  # y value
            self.C_per_base.append(C_val)  # y value
            self.N_per_base.append(N_val)  # y value

            # xval_per_base_seq_and_N_content is the x value

        #
        #

        # 4. Per sequence GC content
        count_GC_content = Counter(sorted(self.GC_content))  # Count the values of GC content of reads

        self.x_GC = list(count_GC_content.keys())  # x value
        self.y_GC = list(count_GC_content.values())  # y value

        #
        #

        # 6. Sequence Length Distribution
        count_len = Counter(sorted(self.read_len))  # Count the values of leangth of reads
        # count = {i: len_data.count(i) for i in len_data_sort}  # Much slower than collections.Counter

        self.x_len = list(count_len.keys())  # x value
        self.y_len = list(count_len.values())  # y value

        print("Preprocessing is done")
        print()

    def get_coordinates_of_per_base_sequence_quality(self) -> dict:
        return {
            "y_val_boxplots": self.read_quality_per_base_cut,  # OY values for boxplots (for each x value)
            "labels_of_x": self.xlab_per_base_seq_qual,  # Name of each x value
            "values_of_x": self.xval_per_base_seq_qual,  # OX values
            "y_val_mean": self.read_quality_per_base_mean  # OY values for mean (for each x value)
        }

    def get_coordinates_of_per_sequence_quality_scores(self) -> dict:
        return {
            "values_of_x":  self.x_per_seq_qual_scores,
            "values_of_y": self.y_per_seq_qual_scores
        }

    def get_coordinates_of_per_base_sequence_content(self) -> dict:
        return {
            "values_of_x": self.xval_per_base_seq_and_N_content,
            "values_of_y_A": self.A_per_base,
            "values_of_y_T": self.T_per_base,
            "values_of_y_G": self.G_per_base,
            "values_of_y_C": self.C_per_base,
        }

    def get_coordinates_of_per_sequence_GC_content(self) -> dict:
        return {
            "values_of_x": self.x_GC,
            "values_of_y": self.y_GC
        }

    def get_coordinates_of_per_base_N_content(self) -> dict:
        return {
            "values_of_x": self.xval_per_base_seq_and_N_content,
            "values_of_y": self.N_per_base
        }

    def get_coordinates_of_sequence_length_distribution(self) -> dict:
        return {
            "values_of_x": self.x_len,
            "values_of_y": self.y_len
        }

