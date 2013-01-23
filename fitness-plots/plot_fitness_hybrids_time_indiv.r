# Get command-line arguments, which must be specified after the '--args' flag
args = commandArgs(T)

if(length(args) < 1)
{
  print('Arguments: fitness_pops_path fitness_hybrids_path output_path title
    legend_location')
  q()
}

fitness_pops_path = args[1]
fitness_hybrids_path = args[2]
output_path = args[3]
title = args[4]
legend_location = args[5]

# Read data (contains column headers)
pops_data = read.table(fitness_pops_path, header = T)
hybrids_data = read.table(fitness_hybrids_path, header = T)

# Setup plot file and basic plot
pdf(file = output_path, width = 4, height = 4.5)

# Split data by populations
pops_data_1 = pops_data[pops_data$Population == 1,]
pops_data_2 = pops_data[pops_data$Population == 2,]
hybrids_data_1 = hybrids_data[hybrids_data$Population == 1,]
hybrids_data_2 = hybrids_data[hybrids_data$Population == 2,]

# Calculate means of populations per replicate
pops_rep_mean_fitness_1 = aggregate(pops_data_1$Fitness,
  by = list(pops_data_1$Replicate, pops_data_1$Update), mean)
names(pops_rep_mean_fitness_1) = c('Replicate', 'Update', 'Fitness')

pops_rep_mean_fitness_2 = aggregate(pops_data_2$Fitness,
  by = list(pops_data_2$Replicate, pops_data_2$Update), mean)
names(pops_rep_mean_fitness_2) = c('Replicate', 'Update', 'Fitness')

hybrids_rep_mean_fitness_1 = aggregate(hybrids_data_1$Fitness,
  by = list(hybrids_data_1$Replicate, hybrids_data_1$Update), mean)
names(hybrids_rep_mean_fitness_1) = c('Replicate', 'Update', 'Fitness')

hybrids_rep_mean_fitness_2 = aggregate(hybrids_data_2$Fitness,
  by = list(hybrids_data_2$Replicate, hybrids_data_2$Update), mean)
names(hybrids_rep_mean_fitness_2) = c('Replicate', 'Update', 'Fitness')

# Calculate relative fitnesses
hybrids_rep_mean_fitness_1$Fitness = 
  hybrids_rep_mean_fitness_1$Fitness / pops_rep_mean_fitness_1$Fitness

hybrids_rep_mean_fitness_2$Fitness = 
  hybrids_rep_mean_fitness_2$Fitness / pops_rep_mean_fitness_2$Fitness

# Rename data variables
data_1 = hybrids_rep_mean_fitness_1
data_2 = hybrids_rep_mean_fitness_2

# Basic plot
plot(0, 0, type = 'n', las = 1, xaxt = 'n',
  main = title,
  xlim = c(0, 10000),
  ylim = c(0.0, 1.0), # Selection & Drift
  #ylim = c(0.5, 2.0), # Mut-order
  xlab = 'Time (updates)',
  ylab = 'Mean hybrid fitness')

xvalues = seq(0, 10000, 2500)
axis(1, at = xvalues,
  labels = prettyNum(xvalues, big.mark = ',', preserve.width = 'individual'))

legend(legend_location,
  legend = c('Hybrids (in deme 1)', 'Hybrids (in deme 2)'),
  lty = c('solid', 'dashed'), col = c('black', 'black'), bty = 'n')

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

dev.off()
