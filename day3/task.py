def isPrimeNum(nums):
  d = dict()
  for n in nums:
    if n > 1:
      for i in range(2, n):
        if n%i == 0:
          break
      else:
        d.setdefault('prime', []).append(n)
  return d

nums = list(range(1, 100))          
print(isPrimeNum(nums))