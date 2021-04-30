
# Напишите генератор, осуществляющий считывание фасты и
# возвращающий по 1-ой оттранслированной последовательности (используйте биопитон)
#
# Принимаемые аргументы функции
#     путь до фасты
#     таблица кодонов - 'Standard' по умолчанию
# Аутпут
#     протеиновый Seq


import Bio.Data.CodonTable
import Bio.Seq
from Bio import SeqIO


def translate_fasta(path_to_fasta: str, table="standart_dna"):
    '''

    :param path_to_fasta:
    :param table:
    :return:
    '''

    if table == "standart_dna":
        codon_table = Bio.Data.CodonTable.standard_dna_table
    elif table == "standart_rna":
        codon_table = Bio.Data.CodonTable.standard_rna_table
    # elif
    # elif

    else:
        raise NameError(f"name {table} is not appropriate codon table. See help ...")

    with open(path_to_fasta) as fasta_data:
        for seq_record in SeqIO.parse(fasta_data, "fasta"):
            sequence = seq_record.seq
            yield sequence.translate(table=codon_table)


with open("./protein_fasta.fasta", "w") as protein_fasta_data:
    for protein_seq in translate_fasta("test.fasta"):
        protein_fasta_data.write(str(protein_seq) + "\n")

# print(next(translate_fasta("test.fasta")))
#
# for test in translate_fasta("test.fasta"):
#     print(test)
#
# print(next(translate_fasta("test.fasta", table="WRONG")))

