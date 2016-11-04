import os
from pydev.dev import sort_bed


def test_sort_bed():
    bed = 'data/t.bed'
    out = 'data/n.bed'
    sort_bed(bed, out)
    with open('data/o.bed', 'r') as r_out, open(out, 'r') as n_out:
        assert r_out.read() == n_out.read(), 'Error!!!'
    os.remove(out)
