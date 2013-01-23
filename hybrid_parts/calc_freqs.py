# Counts the number of times parental halves perform
# certain number of tasks (see code)

import sys


ENV_1 = 2
ENV_2 = 2

TASKS_1 = ['logic_3CI', 'logic_3BO']
TASKS_2 = ['logic_3BH', 'logic_3BJ']

do_mutation_order = (ENV_1 == ENV_2)

# Mutation-order
if do_mutation_order:
  # Mutation-order 1
  if ENV_1 == 1:
    TASK_1 = TASKS_1[0]
    TASK_2 = TASKS_1[1]
    TASK_12 = ' '.join(TASKS_1)
  # Mutation-order 2
  else:
    TASK_1 = TASKS_2[0]
    TASK_2 = TASKS_2[1]
    TASK_12 = ' '.join(TASKS_2)
# Ecological
else:
  TASK_11 = TASKS_1[0]
  TASK_21 = TASKS_1[1]
  TASK_12 = TASKS_2[0]
  TASK_22 = TASKS_2[1]
  TASK_1121 = ' '.join(TASKS_1)
  TASK_1222 = ' '.join(TASKS_2)


def print_counts():
  if do_mutation_order:
    print current_rep, none_count, one_none_count, same_one_count, \
      one_each_count, both_count

#    print current_rep, hybrid_none_count, hybrid_one_count_1, \
#      hybrid_one_count_2, hybrid_two_count

#    print current_rep, intrinsic_count
  else:
    print current_rep, \
      hybrid_none_count, hybrid_one_none_count, hybrid_two_count, \
      hybrid_two_none_count_1, hybrid_two_none_count_2, \
      hybrid_three_count, hybrid_four_count

#    print current_rep, intrinsic_count

def print_header():
  if do_mutation_order:
    print 'Replicate', 'None', 'OneNone', 'SameOne', 'OneOne', 'Both'
    # Hybrid counts
#    print 'Replicate', 'None', 'One_1', 'One_2', 'Two'
  else:
    # Hybrid counts
    print 'Replicate', 'None', 'OneNone', 'OneEach', 'TwoNone_1', \
      'TwoNone_2', 'OneTwo', 'TwoTwo'


if len(sys.argv) < 2:
  print 'Arguments: input_file'
  sys.exit()

input_file = sys.argv[1]

none_count = 0
one_each_count = 0
both_count = 0
one_none_count = 0
same_one_count = 0
unaccounted = 0

# Counts for the number of hybrids
# that can perform a certain number of tasks
hybrid_none_count = 0
hybrid_one_count_1 = 0
hybrid_one_count_2 = 0
hybrid_one_none_count = 0
hybrid_two_count = 0
hybrid_two_none_count_1 = 0
hybrid_two_none_count_2 = 0
hybrid_three_count = 0
hybrid_four_count = 0

# Counts for the number of times a task was present
# in a parental half, but not in the final hybrid
intrinsic_count = 0

print_header()

current_rep = 0
for line in open(input_file):
  line_parts = line.rstrip().split(',')

  replicate = int(line_parts[0])
  parent1tasks = line_parts[1]   # Parent 1 half in env. 1
  parent2tasks = line_parts[2]   # Parent 2 half in env. 2
  hybrid1tasks = line_parts[3]   # Hybrid in env. 1
  hybrid2tasks = line_parts[4]   # Hybrid in env. 2

  # Note: hybrid1tasks should equal hybrid2tasks
  # when environments are the same (i.e., mutation-order)

  if current_rep == 0:
    current_rep = replicate

  if replicate != current_rep:  # New replicate (assumes they are in order)

    print_counts()

    # Reset counts
    none_count = 0
    one_each_count = 0
    both_count = 0
    one_none_count = 0
    same_one_count = 0
    unaccounted = 0

    hybrid_none_count = 0
    hybrid_one_count_1 = 0
    hybrid_one_count_2 = 0
    hybrid_one_none_count = 0
    hybrid_two_count = 0
    hybrid_two_none_count_1 = 0
    hybrid_two_none_count_2 = 0
    hybrid_three_count = 0
    hybrid_four_count = 0

    intrinsic_count = 0

  current_rep = replicate

  # Count intrinsic isolation cases
  parent1tasks_set = set(parent1tasks.split())
  parent2tasks_set = set(parent2tasks.split())
  hybrid1tasks_set = set(hybrid1tasks.split())
  hybrid2tasks_set = set(hybrid2tasks.split())
  if (not parent1tasks_set.issubset(hybrid1tasks_set)) or \
     (not parent2tasks_set.issubset(hybrid2tasks_set)):
    intrinsic_count += 1

  # Mutation-order treatment
  if do_mutation_order:

    # Hybrid cannot perform any tasks
    if hybrid1tasks == '':
      hybrid_none_count += 1
    # Hybrid can only perform the first task
    elif hybrid1tasks == TASK_1:
      hybrid_one_count_1 += 1
    # Hybrid can only perform the second task
    elif hybrid1tasks == TASK_2:
      hybrid_one_count_2 += 1
    # Hybrid can perform both tasks
    elif hybrid1tasks == TASK_12:
      hybrid_two_count += 1
    else:
      unaccounted += 1

    # Consider only those in which the hybrids can do both tasks
    if hybrid1tasks != TASK_12 or hybrid2tasks != TASK_12:
      continue

    # Parent halves cannot do anything
    if parent1tasks == '' and parent2tasks == '':
      none_count += 1
    # Each parent half provides a different task
    elif (parent1tasks == TASK_1 and parent2tasks == TASK_2) \
      or (parent1tasks == TASK_2 and parent2tasks == TASK_1):
      one_each_count += 1
    # At least one parent half provides both tasks
    elif (parent1tasks == TASK_12 or parent2tasks == TASK_12):
      both_count += 1
    # One parent half can perform one task, but the other one none
    elif (parent1tasks == TASK_1 and parent2tasks == '') \
      or (parent1tasks == '' and parent2tasks == TASK_1) \
      or (parent1tasks == TASK_2 and parent2tasks == '') \
      or (parent1tasks == '' and parent2tasks == TASK_2):
      one_none_count += 1
    # Parent halves perform the same one task
    elif (parent1tasks == TASK_1 and parent2tasks == TASK_1) \
      or (parent1tasks == TASK_2 and parent2tasks == TASK_2):
      same_one_count += 1
    else:
      unaccounted += 1

  # Ecological treatment
  else:

    # Hybrids cannot perform any tasks
    if hybrid1tasks == '' and hybrid2tasks == '':
      hybrid_none_count += 1

    # Hybrids can perform one task from one but none from the other
    elif ((hybrid1tasks == TASK_11 or hybrid1tasks == TASK_21) and \
           hybrid2tasks == '') or \
         ((hybrid2tasks == TASK_12 or hybrid2tasks == TASK_22) and \
           hybrid1tasks == ''):
      hybrid_one_none_count += 1

    # Hybrids can perform one task from each environment
    elif (hybrid1tasks == TASK_11 and hybrid2tasks == TASK_12) or \
         (hybrid1tasks == TASK_11 and hybrid2tasks == TASK_22) or \
         (hybrid1tasks == TASK_21 and hybrid2tasks == TASK_12) or \
         (hybrid1tasks == TASK_21 and hybrid2tasks == TASK_22):
      hybrid_two_count += 1

    # Hybrids can perform two from env. 1 but none from the other
    elif (hybrid1tasks == TASK_1121 and hybrid2tasks == ''):
      hybrid_two_none_count_1 += 1

    # Hybrids can perform two from env. 2 but none from the other
    elif (hybrid2tasks == TASK_1222 and hybrid1tasks == ''):
      hybrid_two_none_count_2 += 1

    # Hybrids can perform three tasks
    elif ((hybrid1tasks == TASK_11 or hybrid1tasks == TASK_21) and \
           hybrid2tasks == TASK_1222) or \
         ((hybrid2tasks == TASK_12 or hybrid2tasks == TASK_22) and \
           hybrid1tasks == TASK_1121):
      hybrid_three_count += 1

    # Hybrids can perform all four tasks
    elif hybrid1tasks == TASK_1121 and hybrid2tasks == TASK_1222:
      hybrid_four_count += 1

    if ((parent1tasks == TASK_11 and hybrid1tasks == TASK_11) or \
        (parent1tasks == TASK_21 and hybrid1tasks == TASK_21)) and \
       ((parent2tasks == TASK_12 and hybrid2tasks == TASK_12) or \
        (parent2tasks == TASK_22 and hybrid2tasks == TASK_22)):
      one_each_count += 1
    
# Print last replicate
print_counts()
