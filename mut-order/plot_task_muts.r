# Get command-line arguments, which must be specified after the '--args' flag
args = commandArgs(T)

if(length(args) < 1)
{
  print('Arguments: input_path output_path')
  q()
}

input_path = args[1]
output_path = args[2]

# Read data (contains column headers and blanks)
data = read.table(input_path, header = T, fill = T, stringsAsFactor = F)
summary(data)

# Setup plot file and basic plot
pdf(file = output_path, width = 6, height = 4)
par(mar = c(5, 5, 1, 1))

GENOME_LENGTH = 200

# Basic plot
plot(0, 0, type = 'n', las = 1,
  xlim = c(1, 200),
  ylim = c(0, 40),
  xlab = 'Genome locus',
  ylab = 'Number of demes')

tasks = unique(data$Task)
task_colors = rainbow(length(tasks))

legend('topright', bty = 'n', lty = 'solid', legend = tasks, col = task_colors)

i = 1
for(task in tasks)
{
  task_data = data[data$Task == task,]
  muts = task_data$Mut

#  hist = rep(0, 200)
#  for(mut in muts)
#    hist[mut + 1] = hist[mut + 1] + 1
#  print(hist)

#  lines(seq(200), hist, col = task_colors[i])
  points(jitter(muts), rep(i - 1, length(muts)) * 2, col = task_colors[i])

  i = i + 1
}

dev.off()
