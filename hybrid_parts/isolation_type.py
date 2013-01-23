# Determine the reason hybrids are unfit based on tasks
# (either due to DMIs or task code missing -- see notes 5/24/12)

import sys
import math
import pandas


def main():
  try:
    data_path = sys.argv[1]
  except IndexError:
    print 'Arguments: input_file'
    exit()

  full_data = pandas.read_csv(data_path)

  print 'Replicate', 'DMIs', 'UnfitHybrids'
  for replicate in range(1, 21):
    data = full_data[full_data['Replicate'] == replicate]
    n_DMIs = count_if(data, row_has_DMI)
#   n_missing_alleles = count_if(data, row_has_missing_alleles)
    n_unfit_hybrids = count_if(data, row_has_unfit_hybrid)
#   n_both = count_if(data, row_has_both)

    print replicate, n_DMIs, n_unfit_hybrids
#   print n_missing_alleles
#   print n_both


def count_if(data, condition):
  count = 0
  for row_index, row in data.iterrows():
    if condition(row):
      count += 1
  return count


def row_has_DMI(row):
  hybrid_part_1_tasks, hybrid_part_2_tasks, \
    hybrid_tasks_1, hybrid_tasks_2 = row_tasks(row)
  return hybrid_does_not_do_all_tasks(hybrid_tasks_1, hybrid_tasks_2) and \
      (not hybrid_part_1_tasks.issubset(hybrid_tasks_1) or \
       not hybrid_part_2_tasks.issubset(hybrid_tasks_2))


def row_has_missing_alleles(row):
  hybrid_part_1_tasks, hybrid_part_2_tasks, \
    hybrid_tasks_1, hybrid_tasks_2 = row_tasks(row)
  return hybrid_does_not_do_all_tasks(hybrid_tasks_1, hybrid_tasks_2) and \
      hybrid_does_not_do_all_tasks(hybrid_part_1_tasks, hybrid_part_2_tasks)

def row_has_both(row):
  return row_has_DMI(row) and row_has_missing_alleles(row)


def row_has_unfit_hybrid(row):
  hybrid_part_1_tasks, hybrid_part_2_tasks, \
    hybrid_tasks_1, hybrid_tasks_2 = row_tasks(row)
  return hybrid_does_not_do_all_tasks(hybrid_tasks_1, hybrid_tasks_2)



def row_tasks(row):
  return (tasks(row['HybridPart1Env1']), tasks(row['HybridPart2Env2']), \
    tasks(row['HybridEnv1']), tasks(row['HybridEnv2']))


def tasks(task_string):
  try:
    return set(task_string.split())
  except:    # NaN
    return set()


def hybrid_does_not_do_all_tasks(hybrid_tasks_1, hybrid_tasks_2):
  return less_than_two_tasks(hybrid_tasks_1) or \
      less_than_two_tasks(hybrid_tasks_2)


def less_than_two_tasks(tasks):
  return len(tasks) < 2


def print_row(row):
  hybrid_part_1_tasks, hybrid_part_2_tasks, \
    hybrid_tasks_1, hybrid_tasks_2 = row_tasks(row)
  print 'P1A:', ' '.join(hybrid_part_1_tasks), '|', \
        'P2A:', ' '.join(hybrid_part_2_tasks), '|', \
        'P1P2:', ' '.join(hybrid_tasks_1), ' '.join(hybrid_tasks_2)


main()
