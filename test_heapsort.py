import random
from collections import Counter
import pytest
from heapsort import heapsort




# ---------- Basic tests ----------

def test_empty_list():
    assert heapsort([]) == []


def test_single_element():
    assert heapsort([5]) == [5]


# ---------- Order-related tests ----------

def test_reverse_sorted_input():
    data = [9, 7, 5, 3, 2, -1]
    assert heapsort(data) == sorted(data)


def test_already_sorted_input():
    data = [1, 2, 3, 4, 5, 6]
    assert heapsort(data) == sorted(data)


# ---------- Duplicates & negatives ----------

@pytest.mark.parametrize(
    "data",
    [
        [3, -1, 3, 0, -1, 2],
        [5, 5, 5, 5],
        [-10, -3, -5, -1, -1],
    ],
)
def test_duplicates_and_negatives(data):
    assert heapsort(data) == sorted(data)


# ---------- Floating point numbers ----------

@pytest.mark.parametrize(
    "data",
    [
        [1.5, 2.3, -0.7, 4.1],
        [3.3, 3.3, 1.1, 2.2],
        [-2.5, -3.1, 0.0, 1.8],
    ],
)
def test_floats_and_mixed_numbers(data):
    assert heapsort(data) == sorted(data)


# ---------- Randomized tests ----------

def test_random_lists_repeatable():
    random.seed(42)
    for _ in range(5):
        data = [random.randint(-100, 100) for _ in range(20)]
        assert heapsort(data) == sorted(data)


# ---------- Property-based style test ----------

def test_sorted_and_permutation_properties():
    data = [random.randint(-50, 50) for _ in range(30)]
    result = heapsort(data)

    # Check sorted order
    assert result == sorted(data)

    # Check permutation (same elements)
    assert Counter(result) == Counter(data)




 