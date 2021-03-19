import pytest

from classes_hw.src.Dna_Rna_classes import MyDNA

# init


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [("atgc", "ATGC"), ("A", "A"), ("", ""), ("ggNcc", "GGNCC")],
)
def test_correct_construction_method_of_dna_class(value, expected_result):
    dna = MyDNA(value)
    actual_result = dna.dna
    assert actual_result == expected_result


@pytest.mark.parametrize("value", [1, 1.0, [1, 2], (1, 2), {"1": 2}])
def test_incorrect_construction_method_of_dna_class_with_not_string(value):
    with pytest.raises(TypeError, match="should be a string"):
        MyDNA(value)


@pytest.mark.parametrize("value", ["1", "1.0", "Hi", "AUG", " "])
def test_incorrect_construction_method_of_dna_class_with_not_dna_seq(value):
    with pytest.raises(TypeError, match="(contains A, T, C, G or N)"):
        MyDNA(value)


# GC content


@pytest.mark.parametrize(
    ["value", "expected_result"], [("atgc", 50.0), ("A", 0.0), ("ggcc", 100.0)]
)
def test_correct_gc_content_method_of_dna_class(value, expected_result):
    dna = MyDNA(value)
    actual_result = dna.gc_content()
    assert actual_result == expected_result


def test_incorrect_gc_content_method_of_dna_class_with_empty_str():
    with pytest.raises(ValueError, match="at least one element"):
        MyDNA("").gc_content()


# Reverse_complement


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [("atgc", "TACG"), ("A", "T"), ("ggNcc", "CCNGG"), ("", "")],
)
def test_reverse_complement_method_of_dna_class(value, expected_result):
    dna = MyDNA(value)
    actual_result = dna.reverse_complement()
    assert actual_result == expected_result


# Transcribe


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [("atgc", "AUGC"), ("A", "A"), ("T", "U"), ("ggNcc", "GGNCC"), ("", "")],
)
def test_correct_coding_transcribe_method_of_dna_class(value, expected_result):
    dna = MyDNA(value)
    actual_result = dna.transcribe()
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [("atgc", "UACG"), ("A", "U"), ("ggNcc", "CCNGG"), ("", "")],
)
def test_correct_template_transcribe_method_of_dna_class(value, expected_result):
    dna = MyDNA(value)
    actual_result = dna.transcribe(False)
    assert actual_result == expected_result


@pytest.mark.parametrize("value", [1, 1.0, (1, 2), [1, 2], "False", 0])
def test_incorrect_transcribe_method_of_dna_class_with_wrong_param(value):
    with pytest.raises(TypeError, match="coding should be True or False"):
        MyDNA("atgc").transcribe(value)


# Iterable


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [("atgc", ["A", "T", "G", "C"]), ("A", ["A"]), ("", [])],
)
def test_iterable_of_dna_class(value, expected_result):
    dna = MyDNA(value)
    actual_result = [nucl for nucl in dna]

    assert expected_result == actual_result


# Equal


def test_equal_of_dna_class():
    assert MyDNA("atgc") == MyDNA("atgc")


def test_not_equal_of_dna_class():
    assert MyDNA("atgc") != MyDNA("a")


def test_not_equal_class_vs_str():
    assert MyDNA("ATGC") != "ATGC"


# Hash


def test_hashible_of_dna_class():
    try:
        print(set(MyDNA("atgc")))
        print({MyDNA("atgc"): "smt"})

    except TypeError:
        raise pytest.fail("in hash dna test")
