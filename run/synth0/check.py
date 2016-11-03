#!/usr/bin/env python2.7
import sys
def read_dna(ifs):
    """Assume one contig.
    """
    header = ifs.readline()
    dna = ""
    for line in ifs:
        dna += line.strip()
    return dna
def reverse_complement(dna):
    complement = {"T": "A", "A": "T",
            "G": "C", "C": "G"}
    return ''.join([complement[base] for base in reversed(dna)])
def compare_rot(ref, qry):
    """Compare circular DNA.
    """
    if len(ref) != len(qry):
        raise Exception('%d != %d' %(len(ref), len(qry)))
    for i in range(len(ref)):
        rot = ref[i:] + ref[:i]
        if rot == qry:
            return i
    raise Exception('no match')
def compare_circ(ref, qry):
    """Compare circular DNA.
    """
    try:
        d = 'n'
        shift = compare_rot(ref, qry)
    except Exception:
        d = 'rc'
        shift = compare_rot(reverse_complement(ref), qry)
    print('shifted by %d (%s)' %(shift, d))
def main(prog, ref='data/synth5k/ref.fasta', qry='2-asm-falcon/p_ctg.fa'):
    compare_circ(read_dna(open(ref)), read_dna(open(qry)))

main(*sys.argv)
