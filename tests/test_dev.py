import os
import filecmp
from pydev.dev import sort_bed


def test_sort_bed():
    test_data_path = os.path.abspath(os.path.dirname(__file__))
    bed = os.path.join(test_data_path, 'data/t.bed')
    out = os.path.join(test_data_path, 'data/n.bed')
    sort_bed(bed, out)
    result = os.path.join(test_data_path, 'data/o.bed')
    assert filecmp.cmp(result, out), 'Error!!!'
    os.remove(out)
