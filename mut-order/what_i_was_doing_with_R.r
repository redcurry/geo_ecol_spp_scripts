> data = read.table('prob_intact_tasks.txt', header=T)
> plot(1:20, sapply(lapply(1:20, data_values), mean), type='l', ylim = c(0,1))
> data2 = read.table('temp.txt')
> points(data2$V4, data2$V5, col = 'blue')
> plot(1:20, sapply(lapply(1:20, data_values), mean), type='l')
> points(data2$V4, data2$V5, col = 'blue')
> upper_ci = sapply(lapply(1:20, data_values), quantile, probs=c(0.025,0.975))
> upper_ci
          [,1]     [,2]     [,3]     [,4]     [,5]     [,6]     [,7]     [,8]
2.5%  0.461975 0.229975 0.163000 0.128975 0.104000 0.087975 0.077975 0.068000
97.5% 0.531000 0.488000 0.409075 0.340025 0.278025 0.234000 0.212000 0.186025
          [,9] [,10]    [,11] [,12]    [,13] [,14]    [,15]    [,16]    [,17]
2.5%  0.059000 0.052 0.053000 0.045 0.042000 0.041 0.035975 0.035975 0.031000
97.5% 0.160075 0.145 0.128025 0.117 0.106025 0.099 0.092025 0.088000 0.078025
      [,18] [,19] [,20]
2.5%  0.028 0.028 0.027
97.5% 0.076 0.072 0.068
> ci = upper_ci
> upper_ci=ci["2.5%"]
> upper_ci
[1] NA
> upper_ci=ci["2.5%",]
> upper_ci
 [1] 0.461975 0.229975 0.163000 0.128975 0.104000 0.087975 0.077975 0.068000
 [9] 0.059000 0.052000 0.053000 0.045000 0.042000 0.041000 0.035975 0.035975
[17] 0.031000 0.028000 0.028000 0.027000
> lower_ci=ci["97.5%",]
> plot(1:20, sapply(lapply(1:20, data_values), mean), type='l')
> points(data2$V4, data2$V5, col = 'blue')
> lines(1:20, upper_ci, col='red')
> lines(1:20, lower_ci, col='red')
> plot(1:20, sapply(lapply(1:20, data_values), mean), type='l', ylim = c(0,0.5)) 
> plot(1:20, sapply(lapply(1:20, data_values), mean), type='l', ylim = c(0,0.5), xlim = c(1,20), xlab = 'Number of loci per task', ylab = 'Probability that task is inherited intact')
> plot(1:20, sapply(lapply(1:20, data_values), mean), type='l', ylim = c(0,0.5), xlim = c(0,20), xlab = 'Number of loci needed for a task', ylab = 'Probability that the task is inherited intact')
> plot(1:20, sapply(lapply(1:15, data_values), mean), type='l', ylim = c(0,0.5), xlim = c(0,15), xlab = 'Number of loci needed for a task', ylab = 'Probability that the task is inherited intact')
Error in xy.coords(x, y, xlabel, ylabel, log) : 
  'x' and 'y' lengths differ
> plot(1:15, sapply(lapply(1:15, data_values), mean), type='l', ylim = c(0,0.5), xlim = c(0,15), xlab = 'Number of loci needed for a task', ylab = 'Probability that the task is inherited intact')
> lines(1:20, upper_ci, lty = 'dashed')
> lines(1:20, lower_ci, lty = 'dashed')
> plot(1:15, sapply(lapply(1:15, data_values), mean), type='l', ylim = c(0,0.5), xlim = c(0,15), xlab = 'Number of loci needed for a task', ylab = 'Probability that the task is inherited intact')
> lines(1:15, lower_ci, lty = 'dashed')Error in xy.coords(x, y) : 'x' and 'y' lengths differ
> lines(1:15, lower_ci[1:15], lty = 'dashed')
> lines(1:15, upper_ci[1:15], lty = 'dashed')> points(data2$V4, data2$V5, col = 'blue')
