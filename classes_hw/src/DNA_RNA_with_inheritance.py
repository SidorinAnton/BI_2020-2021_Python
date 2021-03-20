"""
Description of classes with inheritance ...

"""


class _MethodsOfNucleicAcid:
    def gc_content(self, nucleic_acid: str) -> float:
        """
        :return: percentage of GC content
        """

        # Check if len of input dna is 0
        if len(nucleic_acid) == 0:
            raise ValueError("The sequence data should have at least one element")

        g_nucleotide = nucleic_acid.count("G")
        c_nucleotide = nucleic_acid.count("C")

        gc_percent = 100 * (g_nucleotide + c_nucleotide) / len(nucleic_acid)
        return gc_percent

    def reverse_complement(self, nucleic_acid: str, reverse_nucleotides: dict) -> str:
        """
        :return: complementary strand in uppercase
        """
        reverse_nucleotides = reverse_nucleotides
        reverse_sequence = ""
        for nucleotide in nucleic_acid:
            reverse_sequence += reverse_nucleotides[nucleotide]
        return reverse_sequence


class MyDNA(_MethodsOfNucleicAcid):
    def __init__(self, dna_string: str):
        # Check type of dna_string
        if not isinstance(dna_string, str):
            raise TypeError(
                "The sequence data given to a MyDNA object should be a string"
            )

        # Check whether it is MyDNA sequence. Must be A, T, C, G, N
        if not set(dna_string.upper()).issubset({"A", "T", "C", "G", "N"}):
            raise TypeError(
                "The sequence data should be a MyDNA string (contains A, T, C, G or N)"
            )

        self.dna = dna_string.upper()
        self._iteration_index = 0

    def gc_content(self):
        return super().gc_content(self.dna)

    def reverse_complement(self):
        reverse_nucleotides = {"A": "T", "T": "A", "C": "G", "G": "C", "N": "N"}
        return super().reverse_complement(self.dna, reverse_nucleotides)

    def transcribe(self, coding=True) -> str:
        """
        Type of strand could be template or coding.

        Coding strand of MyDNA is a strand, whose base sequence is identical
            to the base sequence of the RNA transcript produced.
        Ex: coding MyDNA - ATGC => RNA - AUGC

        Template strand of MyDNA is a strand, that is copied during the synthesis of mRNA.
        Ex: template MyDNA - ATGC => RNA - UACG

        :param coding: If True, get RNA from coding strand. If False - from template strand
        :return: RNA sequence from MyDNA
        """

        # Check type of param
        if not isinstance(coding, bool):
            raise TypeError(
                "coding should be True or False. If False - get RNA from template strand"
            )

        template_dna_rna = {"A": "U", "T": "A", "C": "G", "G": "C", "N": "N"}
        rna = ""

        if coding:
            for nucleotide in self.dna:
                if nucleotide != "T":
                    rna += nucleotide
                else:  # T
                    rna += "U"
        else:
            for nucleotide in self.dna:
                rna += template_dna_rna[nucleotide]
        return rna

    def __iter__(self):
        return self

    def __next__(self):
        if self._iteration_index != len(self.dna):
            nucleotide = self.dna[self._iteration_index]
            self._iteration_index += 1
            return nucleotide
        raise StopIteration

    def __eq__(self, other):
        if not isinstance(other, MyDNA):
            return False
        return self.dna == other.dna

    def __hash__(self):
        return hash(self.dna)


class MyRNA(_MethodsOfNucleicAcid):
    def __init__(self, rna_string: str):
        # Check type of dna_string
        if not isinstance(rna_string, str):
            raise TypeError(
                "The sequence data given to a MyRNA object should be a string"
            )

        # Check whether it is MyDNA sequence. Must be A, U, C, G, N
        if not set(rna_string.upper()).issubset({"A", "U", "C", "G", "N"}):
            raise TypeError(
                "The sequence data should be a MyRNA string (contains A, U, C, G or N)"
            )

        self.rna = rna_string.upper()
        self._iteration_index = 0

    def gc_content(self):
        return super().gc_content(self.rna)

    def reverse_complement(self):
        reverse_nucleotides = {"A": "U", "U": "A", "C": "G", "G": "C", "N": "N"}
        return super().reverse_complement(self.rna, reverse_nucleotides)

    def __iter__(self):
        return self

    def __next__(self):
        if self._iteration_index != len(self.rna):
            nucleotide = self.rna[self._iteration_index]
            self._iteration_index += 1
            return nucleotide
        raise StopIteration

    def __eq__(self, other):
        if not isinstance(other, MyRNA):
            return False

        return self.rna == other.rna

    def __hash__(self):
        return hash(self.rna)
