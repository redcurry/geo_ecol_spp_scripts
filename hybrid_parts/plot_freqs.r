# Get command-line arguments, which must be specified after the '--args' flag
args = commandArgs(T)

if(length(args) < 1)
{
  print('Arguments: input_path output_path')
  q()
}

input_path = args[1]
output_path = args[2]

# Read data
data = read.table(input_path, header = T)
summary(data)

# Setup plot file and basic plot
pdf(file = output_path, width = 4, height = 4, useDingbats = F)
par(mar = c(5, 5, 1, 1))

# Basic plot
plot(0, 0, type = 'n', las = 1, xaxt = 'n',
  xlim = c(0.75, 4.25),
  ylim = c(0, 500),
  xlab = 'Number of tasks performed\nby each parental component',
  ylab = 'Number of fully fit hybrids')

#legend('bottomright',
#  legend = c('Genetic drift', 'Mutation-order 1', 'Mutation-order 2',
#    'Ecological'),
#  lty = line_types, pch = point_types, bty = 'n')

# Note, I'm not plotting the "same_one" case

xlabels = c('0,0', '1,0', '1,1', '2,*')
axis(1, at = seq(xlabels), labels = xlabels)

for(replicate in data$Replicate)
{
  subdata = data[data$Replicate == replicate,]
  lines(c(subdata$None[1], subdata$OneNone[1], subdata$OneOne[1],
    subdata$Both[1]), col = 'gray')
}

for(replicate in data$Replicate)
{
  subdata = data[data$Replicate == replicate,]
  points(c(subdata$None[1], subdata$OneNone[1], subdata$OneOne[1],
    subdata$Both[1]))
}

# Plot means
means = c(mean(data$None), mean(data$OneNone), mean(data$OneOne),
  mean(data$Both))
segments(x0 = seq(1, 4) - 0.1, x1 = seq(1, 4) + 0.1,
  y0 = means, y1 = means, lwd = 2)

dev.off()
