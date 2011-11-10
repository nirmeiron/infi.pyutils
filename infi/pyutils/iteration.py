from bunch import Bunch
import itertools
from .python_compat import xrange

_NOTHING = object()

def iterate(collection):
    iterator = enumerate(itertools.chain(iter(collection), [_NOTHING]))
    prefetched = _NOTHING

    while True:
        index, element = next(iterator) if prefetched is _NOTHING else prefetched
        if element is _NOTHING:
            break
        prefetched = next(iterator)
        yield Bunch(
            element = element,
            counter0 = index,
            counter1 = index + 1,
            first = (index == 0),
            last  = prefetched[1] is _NOTHING
            )



def renumerate(seq):
    """Like enumerate(), only in reverse order. Useful for filtering a list in place"""
    if isinstance(seq, list) or isinstance(seq, tuple):
        return _renumerate_lazy(seq)
    return _renumerate_strict(seq)

def _renumerate_lazy(seq):
    for index in xrange(len(seq)-1, -1, -1):
        yield index, seq[index]
def _renumerate_strict(seq):
    return reversed(list(enumerate(seq)))
