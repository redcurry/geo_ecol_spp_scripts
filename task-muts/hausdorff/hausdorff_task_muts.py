# Calculates the Hausdorff distance
# between and within (special parameter) sequences

# Note: Hausdorff distance within sequences was a mistake,
#   it doesn't give you "clustering" because two two-locus clusters
#   that are far apart will give a mean distance of 1,
#   ignoring the fact that they are far from each other


import sys

GENOME_LENGTH = 200


def mean(a, b):
  return (a + b) / 2.0


def distance(pos_1, pos_2):
  return min(abs(pos_2 - pos_1), 200 - abs(pos_2 - pos_1))


def hausdorff(set_1, set_2):  # One-way: set_1 to set_2
  if len(set_2) == 0:
    return 0

  d = 0.0
  for pos_1 in set_1:
    if selfFlag:  # Testing itself (skip same positions)
      d += min([distance(pos_1, pos_2) for pos_2 in set_2 if pos_1 != pos_2])
    else:
      d += min([distance(pos_1, pos_2) for pos_2 in set_2])

  if len(set_1) > 0:
    return d / len(set_1)
  else:
    return 0


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


# Additional parameter (anything) to indicate self comparison
selfFlag = False
if len(sys.argv) > 1:
  selfFlag = True


count = 1
for line in sys.stdin:

  line_parts = line.split()
  genotype = line_parts[2]

  muts = get_muts(line_parts)
  muts_1 = muts[0]
  muts_2 = muts[1]

  if count % 2 == 1:
    prev_muts_1 = muts_1
    prev_muts_2 = muts_2
  else:
    if selfFlag:  # Test self (for clustering distance)
      print hausdorff(prev_muts_1, prev_muts_1), \
        hausdorff(prev_muts_2, prev_muts_2)
      print hausdorff(muts_1, muts_1), hausdorff(muts_2, muts_2)
    else:
      print mean(hausdorff(prev_muts_1, muts_1), \
        hausdorff(muts_1, prev_muts_1)),\
        mean(hausdorff(prev_muts_2, muts_2), \
        hausdorff(muts_2, prev_muts_2))

  count += 1
