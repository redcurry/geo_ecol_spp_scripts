bin = function(x)
{
  return(10 - (floor((x - 0.0001)/ (1/9)) + 1))
}

# Get command-line arguments, which must be specified after the '--args' flag
args = commandArgs(T)

if(length(args) < 1)
{
  print('Arguments: input_path output_path anc_parent_fitnesses_path')
  q()
}

input_path = args[1]
output_path = args[2]
anc_parent_fitnesses_path = args[3]

# Replicates to skip (because parents didn't fully adapt)
avoid_replicates = c(3)  # mut-order-1
#avoid_replicates = c(1, 4, 9, 14, 17, 18)  # mut-order-2
#avoid_replicates = c(3, 5, 8, 9)  # selection

# Read data
data = read.table(input_path, header = T)
data = data[!(data$Replicate %in% avoid_replicates),]

# Read ancestral and parental fitness data
anc_parent_data = read.table(anc_parent_fitnesses_path, header = T)
anc_parent_data = anc_parent_data[!(anc_parent_data$Replicate %in% avoid_replicates),]

# Values of interest
anc_fitness = anc_parent_data$AncEnv1[1]
p1_fitnesses = anc_parent_data$AncEnv2 / anc_fitness
p2_fitnesses = anc_parent_data$Parent2Env2 / anc_fitness
hybrid_fitnesses = data$HybridPart2Env2 / anc_fitness

# Setup plot file
pdf(file = output_path, width = 4, height = 4, useDingbats = F)
par(mar = c(5, 5, 1, 1))

# Basic plot
plot(0, 0, type = 'n', las = 1, xaxt = 'n',
  xlim = c(0, 10), ylim = c(1, 3),
  xlab = expression('Hybrid composition ('*P[1]*':'*P[2]*')'),
  ylab = 'Mean hybrid fitness\n(relative to ancestor)',)

xlabels = c(expression(P[1]), '3:1', '1:1', '1:3', expression(P[2]))
axis(1, at = c(0.5, 3, 5, 7, 9.5), labels = xlabels)

for(replicate in unique(data$Replicate))
{
  rep_hybrid_fitness = hybrid_fitnesses[data$Replicate == replicate]
  rep_hybrid_part_1_frac = data[data$Replicate == replicate,]$HybridPart1Frac

  # Bin the parental proportions into bins
  bins = sapply(rep_hybrid_part_1_frac, bin)

  means = aggregate(rep_hybrid_fitness, by = list(bins), mean)
  names(means) = c('Bin', 'Mean')

  p1_fitness = p1_fitnesses[anc_parent_data$Replicate == replicate]
  p2_fitness = p2_fitnesses[anc_parent_data$Replicate == replicate]

  lines(c(0.5, means$Bin, 9.5), c(p1_fitness, means$Mean, p2_fitness),
    col = 'gray')
}

bins = sapply(data$HybridPart1Frac, bin)
means = aggregate(hybrid_fitnesses, by = list(bins), mean)
names(means) = c('Bin', 'Mean')
lines(c(0.5, means$Bin, 9.5),
  c(mean(p1_fitnesses), means$Mean, mean(p2_fitnesses)))

dev.off()
