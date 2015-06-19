#!/usr/bin/env python
from __future__ import division
import sys, os, random
from random import choice

DNA_BASES = ['A', 'C', 'G', 'T']
COMPLEMENT = {
    'A': 'T',
    'C': 'G',
    'G': 'C',
    'T': 'A',
}
complement = lambda x: (COMPLEMENT[base] for base in x)

class DnaCreator(object):
    def Create(self, n):
        return [choice(DNA_BASES) for _ in range(n)]
def WriteSplit(write, seq, split=60):
    nfull = len(seq) // split
    for i in range(nfull):
        slice = seq[i*split:(i+1)*split]
        write(''.join(slice))
        write('\n')
    if nfull < len(seq):
        slice = seq[nfull*split:]
        write(''.join(slice))
        write('\n')
def CircSimulate(dna, writer, cov=20.0, avg=2000):
    class CircSampler(object):
        def Sample(self, tlen, rlen):
            beg = random.randrange(tlen)
            end = beg + rlen
            return beg, end
    dna_len = len(dna)
    circ_dna = dna + dna
    sampler = CircSampler()
    target_total_read_len = dna_len * cov
    total_read_len = 0
    nreads = 0
    while total_read_len < target_total_read_len:
        i = nreads
        beg, end = sampler.Sample(dna_len, avg)
        read = circ_dna[beg:end]
        # Write PB-style.
        writer.write(">m000_000/{0:d}/{1:d}_{2:d}\n".format(i, beg, end))
        WriteSplit(writer.write, read)
        #writer.write(''.join(read))
        #writer.write('\n')
        total_read_len += len(read)
        nreads += 1
        print total_read_len, (total_read_len/target_total_read_len), nreads
    coverage = total_read_len / len(dna)
    avg_read_len = total_read_len / nreads
    sys.stderr.write(repr(locals().keys()))
    sys.stderr.write("""
dna_len={dna_len}
n_zmws={nreads}
avg_read_len={avg_read_len}
total={total_read_len}
coverage={coverage:.1f}x
""".format(**locals()))

def read_dna(ifs):
    header = ifs.readline()
    dna = ""
    for line in ifs:
        dna += line.strip()
    return dna
def main(prog, cov, golden_fasta=None):
    cov = float(cov)
    avg = 2000
    if golden_fasta:
        dna = read_dna(open(golden_fasta))
        dna_len = len(dna)
    else:
        dna_len = 5000
        dna = DnaCreator().Create(dna_len)
    print("dna_len:", dna_len)
    with open('from.fasta', 'w') as dna_writer:
        dna_writer.write(">synthetic/0/0_%d\n" %len(dna))
        dna_writer.write(''.join(dna))
        dna_writer.write("\n")
    with open('cx.ref.fasta', 'w') as ref_writer:
        ref_writer.write(">rand%d\n" %dna_len)
        WriteSplit(ref_writer.write, dna)
    with open('cx.fasta', 'w') as writer:
        #synth(4600000, writer, n_zmws=25000)
        #synth(4, writer, n_zmws=4, avg_read_len=2)
        #synth(40, writer, n_zmws=2, avg_read_len=500)
        CircSimulate(dna, writer, cov=cov, avg=2000)
if __name__ == "__main__":
    main(*sys.argv)
