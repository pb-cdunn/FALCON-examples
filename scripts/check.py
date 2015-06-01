#!/usr/bin/env python
import sys, collections, pprint, itertools
def ranges(covered):
    for c, g in itertools.groupby(covered.items(), lambda x: x[1]):
        indices = [i for i,c in g]
        beg = min(indices)
        end = max(indices) + 1
        yield beg, end, c
def check(iref, ireads):
    """For now, expect a full-line of bases, not split.
    """
    reads = list()
    header = iref.readline()
    n = int(header.split('/')[-1].split('_')[-1])
    dna = iref.readline().strip()
    assert n == len(dna), '%d != %d' %(n, len(dna))
    while True:
        header = ireads.readline()
        if not header:
            break
        beg, end = map(int, header.split('/')[-1].split('_'))
        assert end >= beg
        assert n >= end
        bases = ireads.readline() # discard for now
        reads.append([beg, end])
    reads.sort()
    covered = {i:0 for i in range(n)}
    #collections.defaultdict(int)
    for beg, end in reads:
        #print beg, end, covered[beg]
        for i in range(beg, end):
            covered[i] += 1
    for beg, end, c in ranges(covered):
        if c <=1:
            print beg, end, c
    return
    pprint.pprint(sorted([(i,c) for i,c in covered.items() if c < 3]))
def main(prog, fn_ref, fn_reads):
    """Check lines of 'reads' FASTA vs. 'ref' FASTA.
    """
    with open(fn_ref) as ref, open(fn_reads) as reads:
        check(ref, reads)
if __name__ == "__main__":
    main(*sys.argv)
