import os
import filecmp
import pytest
from pydev.dev import sort_bed, minus


def test_sort_bed(data_folder):
    bed = pytest.helper.data_path('t.bed')
    out = pytest.helper.data_path('n.bed')
    sort_bed(bed, out)
    result = pytest.helper.data_path('o.bed')
    assert filecmp.cmp(result, out), 'Error!!!'
    os.remove(out)


def test_minus():
    assert minus(5, 3) == 2, 'Error!!!'
