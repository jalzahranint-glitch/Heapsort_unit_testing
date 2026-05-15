import random
from collections import Counter
import pytest
from heapsort import heapsort


# ---------- Basic edge cases ----------

def test_empty_list():
    assert heapsort([]) == []


def test_single_element():
    assert heapsort([42]) == [42]


def test_all_equal_elements():
    data = [5, 5, 5, 5]
    assert heapsort(data) == sorted(data)


# ---------- Order-related edge cases ----------

def test_reverse_sorted_input():
    data = [9, 7, 5, 3, 1, -1]
    assert heapsort(data) == sorted(data)


def test_already_sorted_input():
    data = [1, 2, 3, 4, 5, 6]
    assert heapsort(data) == sorted(data)


# ---------- Duplicates & negatives ----------

@pytest.mark.parametrize(
    "data",
    [
        [3, -1, 3, 0, -1, 2],
        [-5, -10, -3, -5],
        [0, 0, 0, -1, 1],
    ],
)
def test_duplicates_and_negatives(data):
    assert heapsort(data) == sorted(data)


# ---------- Floating-point values ----------

@pytest.mark.parametrize(
    "data",
    [
        [1.5, 2.3, -0.7, 4.1],
        [3.14, 2.71, 1.41, 0.0],
        [-1.1, -2.2, 3.3],
    ],
)
def test_floats_and_mixed_numbers(data):
    assert heapsort(data) == sorted(data)


# ---------- Randomized tests ----------

def test_random_lists_repeatable():
    random.seed(42)
    for _ in range(10):
        data = [random.randint(-100, 100) for _ in range(20)]
        assert heapsort(data) == sorted(data)


# ---------- Property-based checks ----------

def test_sorted_and_permutation_properties():
    data = [random.randint(-50, 50) for _ in range(30)]
    result = heapsort(data)

    # Property 1: output is sorted
    assert result == sorted(data)

    # Property 2: elements are preserved (permutation)
    assert Counter(result) == Counter(data)
