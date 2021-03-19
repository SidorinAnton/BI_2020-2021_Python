import pytest

from classes_hw.src.DNA_RNA_with_inheritance import MyRNA

# init


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [("augc", "AUGC"), ("A", "A"), ("", ""), ("uuNcc", "UUNCC")],
)
def test_correct_construction_method_of_rna_class(value, expected_result):
    rna = MyRNA(value)
    actual_result = rna.rna
    assert actual_result == expected_result


@pytest.mark.parametrize("value", [1, 1.0, [1, 2], (1, 2), {"1": 2}])
def test_incorrect_construction_method_of_rna_class_with_not_string(value):
    with pytest.raises(TypeError, match="should be a string"):
        MyRNA(value)


@pytest.mark.parametrize("value", ["1", "1.0", "Hi", "ATG", " "])
def test_incorrect_construction_method_of_rna_class_with_not_rna_seq(value):
    with pytest.raises(TypeError, match="(contains A, U, C, G or N)"):
        MyRNA(value)


# GC content


@pytest.mark.parametrize(
    ["value", "expected_result"], [("augc", 50.0), ("A", 0.0), ("ggcc", 100.0)]
)
def test_correct_gc_content_method_of_rna_class(value, expected_result):
    rna = MyRNA(value)
    actual_result = rna.gc_content()
    assert actual_result == expected_result


def test_incorrect_gc_content_method_of_rna_class_with_empty_str():
    with pytest.raises(ValueError, match="at least one element"):
        MyRNA("").gc_content()


# Reverse_complement


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [("augc", "UACG"), ("A", "U"), ("ggNcc", "CCNGG"), ("", "")],
)
def test_reverse_complement_method_of_rna_class(value, expected_result):
    rna = MyRNA(value)
    actual_result = rna.reverse_complement()
    assert actual_result == expected_result


# Iterable


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [("augc", ["A", "U", "G", "C"]), ("A", ["A"]), ("", [])],
)
def test_iterable_of_rna_class(value, expected_result):
    rna = MyRNA(value)
    actual_result = [nucl for nucl in rna]

    assert expected_result == actual_result


# Equal


def test_equal_of_rna_class():
    assert MyRNA("augc") == MyRNA("augc")


def test_not_equal_of_rna_class():
    assert MyRNA("augc") != MyRNA("a")


def test_not_equal_class_rna_vs_str():
    assert MyRNA("AUGC") != "AUGC"


# Hash


def test_hashible_of_rna_class():
    try:
        smt_set = set(MyRNA("augc"))
        smt_dict = {MyRNA("augc"): "smt"}

    except TypeError:
        raise pytest.fail("in hash rna test")
