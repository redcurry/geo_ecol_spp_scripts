# For every combination of the ability to perform tasks
# count the number of cases for hybrids and parental components

# Data files are in the data directory, where fitnesses are given,
# so I must also guess as to the number of tasks based on fitnesses


import sys
import csv


# Fitnesses for the number of tasks performed
N_TASKS_FITNESS = [0.28, 0.55, 0.82]

DATA_IS_ECOLOGICAL = False


def main():
  try:
    data_path = sys.argv[1]
  except:
    print 'Arguments: data_path'
    exit(1)

  data = read_data(data_path)

  if DATA_IS_ECOLOGICAL:
    print 'HybridPart1Env1', 'HybridPart2Env2', 'HybridEnv1', 'HybridEnv2', 'Frac'
  else:
    print 'HybridPart1Env1', 'HybridPart2Env2', 'Hybrid', 'Frac'

  for n_tasks_1 in [0, 1, 2]:
    for n_tasks_2 in [0, 1, 2]:
      for n_tasks_hy1 in [0, 1, 2]:
        # If data is ecological, look at hybrids under second environment
        if DATA_IS_ECOLOGICAL:
          for n_tasks_hy2 in [0, 1, 2]:
            cases = count_cases(data, n_tasks_1, n_tasks_2, n_tasks_hy1, n_tasks_hy2)
            print n_tasks_1, n_tasks_2, n_tasks_hy1, n_tasks_hy2, cases / 20000.0
        else:
          cases = count_cases(data, n_tasks_1, n_tasks_2, n_tasks_hy1, n_tasks_hy1)
          print n_tasks_1, n_tasks_2, n_tasks_hy1, cases / 20000.0


def read_data(path):
  csv_reader = csv.reader(open(path), delimiter=' ')
  headers = csv_reader.next()
  data = init_data(headers)
  for row in csv_reader:
    add_data(data, headers, row)
  return data


def init_data(headers):
  data = {}
  for header in headers:
    data[header] = []
  return data


def add_data(data, headers, row):
  for col in range(len(row)):
    data[headers[col]].append(float(row[col]))


def count_cases(data, n_tasks_1, n_tasks_2, n_tasks_hy1, n_tasks_hy2):
  cases = 0
  data_length = len(data['Replicate'])
  for row_i in range(data_length):
    if guess_n_tasks(data['HybridPart1Env1'][row_i]) == n_tasks_1 and \
       guess_n_tasks(data['HybridPart2Env2'][row_i]) == n_tasks_2 and \
       guess_n_tasks(data['HybridEnv1'][row_i]) == n_tasks_hy1 and\
       guess_n_tasks(data['HybridEnv2'][row_i]) == n_tasks_hy2:
      cases += 1
  return cases


def guess_n_tasks(fitness):
  min_diff = 1.0
  min_diff_i = 0
  for n_task_fitness_i in range(len(N_TASKS_FITNESS)):
    diff = abs_diff(fitness, N_TASKS_FITNESS[n_task_fitness_i])
    if diff < min_diff:
      min_diff = diff
      min_diff_i = n_task_fitness_i
  return min_diff_i


def abs_diff(x, y):
  return abs(x - y)


main()
