import sys

if len(sys.argv) < 2:
  print 'Arguments: sequence_1 sequence_2'
  exit(1)

sequence_1 = sys.argv[1]
sequence_2 = sys.argv[2]

distance = 0
for pos in range(len(sequence_1)):
  if sequence_1[pos] != sequence_2[pos]:
    distance += 1

print float(distance) / len(sequence_1)
