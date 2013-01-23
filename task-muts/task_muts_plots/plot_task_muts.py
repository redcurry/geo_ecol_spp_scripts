# Creates an HTML 'plot' of the mutations that perform tasks

def print_task_mut(task, inst):
  sys.stdout.write('<span class="')

  if task == task_3CI:
    sys.stdout.write('task_3CI')
  elif task == task_3BO:
    sys.stdout.write('task_3BO')
  elif task == task_3BH:
    sys.stdout.write('task_3BH')
  elif task == task_3BJ:
    sys.stdout.write('task_3BJ')
  elif task == task_3CI + task_3BO:
    sys.stdout.write('task_3CI_3BO')
  elif task == task_3BH + task_3BJ:
    sys.stdout.write('task_3BH_3BJ')
  else:
    print 'Error: Task not found'

  sys.stdout.write('">')
  sys.stdout.write(inst)
  sys.stdout.write('</span>')

import sys

task_3CI = 'logic_3CI'
task_3BO = 'logic_3BO'

task_3BH = 'logic_3BH'
task_3BJ = 'logic_3BJ'

color_3CI = 'blue'
color_3BO = 'red'
color_3CI_3BO = 'purple'

color_3BH = 'green'
color_3BJ = 'orange'
color_3BH_3BJ = 'yellow'


print '<html>'
print '<head>'
print '<style type="text/css">'
print '* { font-family: Courier; }'
print '.task_3CI { background-color:', color_3CI, '; }'
print '.task_3BO { background-color:', color_3BO, '; }'
print '.task_3CI_3BO { background-color:', color_3CI_3BO, '; }'
print '.task_3BH { background-color:', color_3BH, '; }'
print '.task_3BJ { background-color:', color_3BJ, '; }'
print '.task_3BH_3BJ { background-color:', color_3BH_3BJ, '; }'
print '</style>'
print '</head>'
print '<body>'

for line in sys.stdin:

  line_parts = line.split()

  genotype = line_parts[2]

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

  for pos in range(len(genotype)):
    inst = genotype[pos]
    if pos in muts_1:
      if pos in muts_2:
        print_task_mut(task_1 + task_2, inst)
      else:
        print_task_mut(task_1, inst)
    elif pos in muts_2:
      print_task_mut(task_2, inst)
    else:
      sys.stdout.write(inst)
  print

print '</body>'
print '</html>'
