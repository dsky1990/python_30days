# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b)
#         a, b = b, a + b
#         n = n + 1
#     else:
#       print('done')

# fib(9)    

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    return "done"

n = fib(10)

while True:
  try:
    x = next(n)
    print("n:%d" %x)
  except StopIteration as e:
    print("Generation return value:", e.value)
    break      
