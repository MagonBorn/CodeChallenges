def fibonacciModified(t1, t2, n):
  # Write code here
  for i in range(n-2):
      t3 = t1 + (t2)**2
      t1 = t2
      t2 = t3
  return t3

result = fibonacciModified(0, 1, 6)
print(result)