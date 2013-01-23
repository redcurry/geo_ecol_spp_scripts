# Get command-line arguments, which must be specified after the '--args' flag
args = commandArgs(T)

if(length(args) < 1)
{
  print('Arguments: input_path output_path')
  q()
}

input_path = args[1]
output_path = args[2]

# Specify here whether data is mut-order or selection
#data_type = 'mut-order'
data_type = 'selection'  # also change the pdf size to 6, 4

# Read data
data = read.table(input_path, header = T)
summary(data)

# Setup plot file
pdf(file = output_path, width = 6, height = 4, useDingbats = F)
par(mar = c(5, 5, 1, 1))

if(data_type == 'mut-order') {

  # Basic plot
  plot(0, 0, type = 'n', las = 1, xaxt = 'n',
    xlim = c(0.75, 4.25), ylim = c(0, 1000),
    xlab = 'Task(s) performed by hybrid',
    ylab = 'Number of hybrids')
  xlabels = c('None', '1', '2', '1 and 2')
  axis(1, at = seq(xlabels), labels = xlabels)

  # Plot lines
  for(replicate in data$Replicate)
  {
    subdata = data[data$Replicate == replicate,]
    lines(c(subdata$None, subdata$One_1, subdata$One_2, subdata$Two),
      col = 'gray')
  }

  # Plot points
  for(replicate in data$Replicate)
  {
    subdata = data[data$Replicate == replicate,]
    points(c(subdata$None, subdata$One_1, subdata$One_2, subdata$Two))
  }

  # Plot means
  means = c(mean(data$None), mean(data$One_1), mean(data$One_2), mean(data$Two))
  segments(x0 = seq(1, 4) - 0.1, x1 = seq(1, 4) + 0.1,
    y0 = means, y1 = means, lwd = 2)

} else {

  # Basic plot
  plot(0, 0, type = 'n', las = 1, xaxt = 'n',
    xlim = c(0.75, 6.25), ylim = c(0, 500),
    xlab = 'Number of tasks performed by hybrid in each environment',
    ylab = 'Number of hybrids')
  xlabels = c('0-0', '1-0', '1-1', '2-0', '2-1', '2-2')
  axis(1, at = seq(xlabels), labels = xlabels)

  # Plot lines
  for(replicate in data$Replicate)
  {
    subdata = data[data$Replicate == replicate,]
    subdata_TwoNone = subdata$TwoNone_1 + subdata$TwoNone_2
    lines(c(subdata$None, subdata$OneNone, subdata$OneEach, subdata_TwoNone,
      subdata$OneTwo, subdata$TwoTwo), col = 'gray')
  }

  # Plot points
  for(replicate in data$Replicate)
  {
    subdata = data[data$Replicate == replicate,]
    subdata_TwoNone = subdata$TwoNone_1 + subdata$TwoNone_2
    points(c(subdata$None, subdata$OneNone, subdata$OneEach, subdata_TwoNone,
      subdata$OneTwo, subdata$TwoTwo))
  }

  # Plot means
  means = c(mean(data$None), mean(data$OneNone), mean(data$OneEach),
    mean(data$TwoNone_1 + data$TwoNone_2), mean(data$OneTwo), mean(data$TwoTwo))
  segments(x0 = seq(1, 6) - 0.1, x1 = seq(1, 6) + 0.1,
    y0 = means, y1 = means, lwd = 2)
}

dev.off()
