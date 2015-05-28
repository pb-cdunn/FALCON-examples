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
def synth(dna_len, ref_writer, dna_writer, writer, n_zmws=100):
    '''
    Writer FASTA files:
        ref_writer: reference (source DNA)
        writer: all "reads"
    '''
    min_read_len = 25 # imposed by DALIGNER
    class DnaCreator(object):
        def Create(self, n):
            return [choice(DNA_BASES) for _ in range(n)]
    class Loader(object):
        worst_len = 500
        best_len = 1500
        def __init__(self, n_zmws):
            self.n_zmws = n_zmws
        def Load(self):
            worst_len = self.worst_len
            best_len = self.best_len
            n_zmws = self.n_zmws
            tlen = len(dna)
            for i in range(self.n_zmws):
                rlen = random.randrange(worst_len, best_len + 1)
                beg = random.randrange(rlen + len(dna)) - rlen
                end = beg + rlen
                beg = max(0, beg)
                end = min(end, tlen)
                if end - beg >= min_read_len:
                    yield (i, beg, end)
    class Ringer(object):
        def Ring(self, i, beg, end):
            capA = []
            capB = []
            ring = dna[beg:end] + capA + list(complement(reversed(dna[beg:end]))) + capB
            return ring
    class Sampler(object):
        def Read(self, seq, upton):
            l = len(seq)
            if upton >= l:  # == b/c randrange(0) fails
                return seq
            curr = random.randrange(l-upton)
            return seq[curr:curr+upton]
    class MessyReader(object):
        erate = .0
        def Read(self, seq):
            '''No inserts or deletes yet.
            (And we under-shoot erate by choice(DNA_BASES).)
            '''
            dist = random.uniform
            choice = random.choice
            erate = self.erate
            return [b if dist(0, 1) > erate else choice(DNA_BASES) for b in seq]
            #return [b for b in seq if dist(0, 1) > erate]
    class RingReader(object):
        def Read(self, ring, n):
            '''No inserts or deletes yet.
            '''
            l = len(ring)
            curr = random.randrange(l)
            while n:
                yield ring[curr]
                curr += 1
                if curr == l:
                    curr = 0
                n -= 1
    dna = DnaCreator().Create(dna_len)
    ref_writer.write(">rand%d\n" %dna_len)
    dna_writer.write(">synthetic/0/0_%d\n" %len(dna))
    dna_writer.write(''.join(dna))
    dna_writer.write("\n")
    WriteSplit(ref_writer.write, dna)
    loader = Loader(n_zmws)
    #ringer = Ringer()
    reader = MessyReader()
    total_read_len = 0
    nreads = 0
    for i, beg, end in loader.Load():
        #print dna[beg:end]
        #ring = ringer.Ring(i, beg, end)
        ##print ring
        #n = random.randrange(min_read_len, avg_read_len * 2)
        #read = list(reader.Read(ring, n))
        #read = list(reader.Read(dna[beg:end], n))
        #read = dna[beg:end]
        read = list(reader.Read(dna[beg:end]))
        if len(read) < min_read_len:
            continue
        #writer.write(">m000_000/{0:d}/garbage/{1:d}_{2:d}\n".format(i, 0, len(read)))
        # >m140913_050931_42139_c100713652400000001823152404301535_s1_p0/9/1607_26058 RQ=0.831
        writer.write(">m000_000/{0:d}/{1:d}_{2:d}\n".format(i, beg, end))
        writer.write(''.join(read))
        writer.write('\n')
        total_read_len += len(read)
        nreads += 1
    coverage = total_read_len / dna_len
    avg_read_len = total_read_len / nreads
    sys.stderr.write(repr(locals().keys()))
    sys.stderr.write("""
dna_len={dna_len}
n_zmws={n_zmws}
avg_read_len={avg_read_len}
total={total_read_len}
coverage={coverage:.1f}x
""".format(**locals()))
        
    #reader = PbReader(dna)
def main():
    with open('cx.ref.fasta', 'w') as ref_writer,\
         open('cx.fasta', 'w') as writer,\
         open('from.fasta', 'w') as dna_writer:
        #synth(4600000, ref_writer, dna_writer, writer, n_zmws=25000)
        #synth(4, ref_writer, writer, n_zmws=4, avg_read_len=2)
        #synth(40, ref_writer, writer, n_zmws=2, avg_read_len=500)
        #synth(500000, ref_writer, dna_writer, writer, n_zmws=14000)
        synth(500000, ref_writer, dna_writer, writer, n_zmws=14000)
if __name__ == "__main__":
    main()
