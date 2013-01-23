# Get command-line arguments, which must be specified after the '--args' flag
args = commandArgs(T)

if(length(args) < 1)
{
  print('Arguments: fitness_pops_path output_path title legend_location')
  q()
}

fitness_pops_path = args[1]
output_path = args[2]
title = args[3]
legend_location = args[4]

# Read data (contains column headers)
data = read.table(fitness_pops_path, header = T)

# Setup plot file
pdf(file = output_path, width = 4, height = 4.5)

# Get the ancestor's fitness and make fitnesses relative
ancestor_fitness = mean(data[data$Update == 1, "Fitness"])
data$Fitness = data$Fitness / ancestor_fitness

# Split data by populations
data_1 = data[data$Population == 1,]
data_2 = data[data$Population == 2,]

replicate_mean_fitness_1 =
  aggregate(data_1$Fitness, by = list(data_1$Replicate, data_1$Update), mean)
names(replicate_mean_fitness_1) = c('Replicate', 'Update', 'Fitness')

replicate_mean_fitness_2 =
  aggregate(data_2$Fitness, by = list(data_2$Replicate, data_2$Update), mean)
names(replicate_mean_fitness_2) = c('Replicate', 'Update', 'Fitness')

data_1 = replicate_mean_fitness_1
data_2 = replicate_mean_fitness_2

# Set up plot
plot(0, 0, type = 'n', las = 1, xaxt = 'n',
  main = title,
  xlim = c(0, 10000),
  ylim = c(1, 9),
  xlab = 'Time (updates)',
  ylab = 'Relative fitness')

xvalues = seq(0, 10000, 2500)
axis(1, at = xvalues,
  labels = prettyNum(xvalues, big.mark = ',', preserve.width = 'individual'))

replicates = sort(unique(data_1$Replicate))

colors = rainbow(length(replicates))

for(rep in replicates)
{
  plot_data_1 = data_1[data_1$Replicate == rep,]
  plot_data_2 = data_2[data_2$Replicate == rep,]

  lines(plot_data_1$Update, plot_data_1$Fitness,
    col = colors[rep], lty = 'solid')
  lines(plot_data_2$Update, plot_data_2$Fitness,
    col = colors[rep], lty = 'dashed')
}

legend(legend_location, legend = c('Deme 1', 'Deme 2'),
  lty = c('solid', 'dashed'), col = c('black', 'black'), bty = 'n')

dev.off()
