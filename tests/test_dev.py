import os
import filecmp
from pydev.dev import sort_bed


def test_sort_bed():
    bed = 'data/t.bed'
    out = 'data/n.bed'
    sort_bed(bed, out)
    result = 'data/o.bed'
    assert filecmp.cmp(result, out), 'Error!!!'
    os.remove(out)
