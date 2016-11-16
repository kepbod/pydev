import os
import filecmp
import pytest
from pydev.dev import sort_bed, minus


@pytest.fixture
def data_folder():
    return os.path.abspath(os.path.dirname(__file__))


def test_sort_bed(data_folder):
    bed = os.path.join(data_folder, 'data/t.bed')
    out = os.path.join(data_folder, 'data/n.bed')
    sort_bed(bed, out)
    result = os.path.join(data_folder, 'data/o.bed')
    assert filecmp.cmp(result, out), 'Error!!!'
    os.remove(out)


def test_minus():
    assert minus(5, 3) == 2, 'Error!!!'
