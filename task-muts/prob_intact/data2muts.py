# Converts a data file (in data directory)
# to a list of mutations (for the prob_task_intact program)


import sys

GENOME_LENGTH = 200


def get_muts(line_parts):
  task_1 = line_parts[4]
  n_muts_1 = int(line_parts[5])
  if n_muts_1 > 0:
    muts_1 = [int(x) for x in line_parts[6:(6 + n_muts_1)]]
  else:
    muts_1 = []

  task_2 = line_parts[6 + n_muts_1]
  n_muts_2_start = 6 + n_muts_1 + 1
  n_muts_2 = int(line_parts[n_muts_2_start])
  if n_muts_2 > 0:
    muts_2 = [int(x) for x in
      line_parts[n_muts_2_start + 1:(n_muts_2_start + 1 + n_muts_2)]]
  else:
    muts_2 = []

  return [muts_1, muts_2]


# Optional parameter indicating the task number (1 or 2)
task_num = 0
if len(sys.argv) > 1:
  task_num = int(sys.argv[1])

for line in sys.stdin:

  line_parts = line.split()
  genotype = line_parts[2]

  muts = get_muts(line_parts)
  muts_1 = muts[0]
  muts_2 = muts[1]

  print GENOME_LENGTH,

  if task_num == 0 or task_num == 1:
    for pos in muts_1: print pos,
    print

  if task_num == 0 or task_num == 2:
    for pos in muts_2: print pos,
    print
