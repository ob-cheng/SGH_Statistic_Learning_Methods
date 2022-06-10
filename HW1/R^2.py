import matplotlib.pyplot as plot
import numpy
from scipy.stats import linregress
import time
#-----------------------------------------------------------

def r_sq(n):
    x = numpy.random.normal(loc=0.0, scale=1.0, size=n)
    y = 1 + x + numpy.random.normal(loc=0.0, scale=1.0, size=n)
    res = linregress(x, y)
    return res.rvalue ** 2
#-----------------------------------------------------------

sizes = list(range(10, 200, 10))
reps = 10000
r_squared_q95 = numpy.zeros(len(sizes))
r_squared_q5 = numpy.zeros(len(sizes))
r_squared_mean = numpy.zeros(len(sizes))
start_time = time.time()
#-----------------------------------------------------------

for idx, val in enumerate(sizes):
    print(idx, val)
    result = [r_sq(val) for _ in range(reps)]
    r_squared_mean[idx] = numpy.mean(result)
    r_squared_q5[idx] = numpy.quantile(result, 0.05)
    r_squared_q95[idx] = numpy.quantile(result, 0.95)

print('-----------------------------------------------------------')
print("time: %s sec" % round((time.time() - start_time), 2))

plot.ylim([min(r_squared_q5), max(r_squared_q95)])
plot.scatter(sizes, r_squared_mean)
plot.plot(sizes, r_squared_q5)
plot.plot(sizes, r_squared_q95)
plot.show()
