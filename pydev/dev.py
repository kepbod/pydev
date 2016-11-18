from pybedtools import BedTool


def add(x, y):
    '''
    >>> add(10, 20)
    30
    '''
    return x + y


def minus(x, y):
    '''
    X - Y
    '''
    return x - y


def sort_bed(fn, out):
    '''
    Sort bed files
    '''
    bed = BedTool(fn)
    sorted_bed = bed.sort()
    sorted_bed.saveas(out)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
