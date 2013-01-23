# Prints the heterozygosity at every locus of the given population (stdin)


import sys


# Create a list from 'a' to 'z'
INSTRUCTIONS = [chr(x) for x in range(ord('a'), ord('z') + 1)]


def calc_allele_freqs(pop, locus):

  allele_freqs = get_empty_allele_freqs()

  # Count number of occurrences of each allele
  for genotype in pop:
    inst = genotype[locus]
    allele_freqs[inst] += 1.0

  # Calculate frequencies from counts
  pop_size = len(pop)
  for inst in allele_freqs:
    allele_freqs[inst] /= pop_size

  return allele_freqs


def get_empty_allele_freqs():

  allele_freqs = {}
  for inst in INSTRUCTIONS:
    allele_freqs[inst] = 0.0
  return allele_freqs


def calc_heterozygosity(pop, locus):

  # Get allele frequencies as a dictionary, e.g., {a: 0.8, b: 0.2}
  allele_freqs = calc_allele_freqs(pop, locus)

  # Calculate the sum of squares of allele frequencies
  ss = calc_sum_of_squares(allele_freqs.values())

  return 1 - ss


def calc_sum_of_squares(values):

  return sum([x * x for x in values])


# Read genotypes from stdin
pop = [genotype.strip() for genotype in sys.stdin]

genotype_length = len(pop[0])
for locus in range(genotype_length):
  heterozygosity = calc_heterozygosity(pop, locus)
  print heterozygosity
