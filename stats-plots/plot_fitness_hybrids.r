bootstrap_ci = function(x, n = 100, lower = 0.025, upper = 0.975)
{
  means = replicate(n, mean(sample(x, replace = T)))
  quantile(means, probs = c(lower, upper))
}

get_box = function(x)
{
  ci = bootstrap_ci(x)
  c(ci[1], mean(x), ci[2])
}

get_hybrid_box = function(mig, data)
{
  get_box(data[data$Migration == mig,]$Fitness)
}

errorbars = function(x, y, upper, lower)                                        
{                                                                               
  arrows(x, upper, x, lower, length = 0.025, angle = 90, code = 3)
}

migtext2labels = function(mig)
{
  if(mig == 'm-0.0')
    return('0.0')
  else if(mig == 'm-0.001')
    return('0.001')
  else if(mig == 'm-0.0001')
    return('0.0001')
  else if(mig == 'm-0.00001')
    return('0.00001')
  else if(mig == 'm-0.01')
    return('0.01')
  else if(mig == 'm-0.05')
    return('0.05')
  else if(mig == 'm-0.1')
    return('0.1')
  else if(mig == 'm-0.5')
    return('0.5')
  else
    return('err')
}

# Get command-line arguments, which must be specified after the '--args' flag
args = commandArgs(T)

if(length(args) < 1)
{
  print('Arguments: fitness_summary_path output_path')
  q()
}

fitness_summary_path = args[1]
output_path = args[2]

# Read data (contains column headers)
data = read.table(fitness_summary_path, header = T)
summary(data)

# Setup plot file and basic plot
pdf(file = output_path, width = 6, height = 3.33, useDingbats = F)
par(mar = c(5, 5, 1, 1), cex = 0.9)

# Basic plot
plot(0, 0, type = 'n', las = 1, xaxt = 'n',
  xlim = c(1, 8),
  ylim = c(0, 1),
  xlab = 'Migration rate',
  ylab = 'Mean hybrid fitness')

# Set up line and point types
line_types = c('solid', 'dashed', 'dotted', 'dotdash')
point_types = c(0, 16, 17, 5)

legend('bottomright',
  legend = c('Genetic drift', 'Mutation-order 1', 'Mutation-order 2',
    'Ecological'),
  lty = line_types, pch = point_types, bty = 'n')

migs = unique(data$Migration)
migs = migs[2:length(migs)] # Remove the control
mig_labels = sapply(migs, migtext2labels)

axis(1, at = seq(mig_labels), labels = mig_labels)

line_type_ix = 1

treatments = unique(data$Treatment)
for(treatment in treatments)
{
  treat_data = data[data$Treatment == treatment,]

  print(treatment)

  demes = unique(treat_data$Deme)
#  for(deme in demes)  # Ignore demes (pool deme hybrid fitnesses together)
  {
#    deme_data = treat_data[treat_data$Deme == deme,]
    deme_data = treat_data

    hybrid_box = sapply(migs, get_hybrid_box, deme_data)

    hybrid_lower = hybrid_box[1,]
    hybrid_mean  = hybrid_box[2,]
    hybrid_upper = hybrid_box[3,]

    lines(seq(mig_labels), hybrid_mean, lty = line_types[line_type_ix])
    points(seq(mig_labels), hybrid_mean, pch = point_types[line_type_ix])

    errorbars(seq(mig_labels), hybrid_mean, hybrid_lower, hybrid_upper)

    print(line_types[line_type_ix])
    print(cbind(hybrid_mean, hybrid_lower, hybrid_upper))
  }

  line_type_ix = line_type_ix + 1
}

dev.off()
