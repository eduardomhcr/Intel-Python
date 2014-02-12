# Programa TPK
import math
 
def f(x):
  return math.sqrt(abs(x)) + 5 * x**3
 
vals = [float(input()) for i in range(11)]
for i, x in enumerate(reversed(vals)):
  y = f(x)
  print('{0}: {1}'.format(i, y if y <= 400 else 'TOO LARGE'))