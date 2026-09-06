from fasta_parser import parse_fasta
from gff_parser import parse_gff
from train import est_emission, est_transition
from viterbi import viterbi

# parse fasta to raw nucleotides
genome = parse_fasta("../data/sequence.fasta")
# parse gff to coding/non-coding annotation
annotation = parse_gff("../data/annotation.gff", len(genome))

# train model on first 500k nucleotides; run model on whole genome
training_genome = genome[:500000]
training_annotation = annotation[:500000]

# estimate emission and transition probabilities
eprobs = est_emission(training_genome, training_annotation)
tprobs = est_transition(training_annotation)

# placeholder probabilities
iprobs = {"C": 0.5, "N": 0.5}

# run viterbi alg
predicted = viterbi(genome, iprobs, tprobs, eprobs)

print(predicted)
