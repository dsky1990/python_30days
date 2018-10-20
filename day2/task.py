# num = int(input("输入数字1-10之前的数字\t"))
# if num > 7:
#   print("%d > 7" %num)
# elif num < 4:
#   print("%d < 4" %num)
# else:
#     print("3 < %d < 8" %num)  
      
# count = 0
# while count < 5:
#   print(count, "< 5")
#   count += 1
# else:
#     print(count, ">= 5")

# name = "python"

# for x in name:
#   print(x)

# sites = ["Baidu", "Google","Runoob","Taobao"]
# for site in sites:
#   if site == 'Runoob':
#     print('Runoob')
#     break
#   print("round %s" %site)
# else:
#   print("no data")
# print("done")      

# sites = ["Baidu", "Google","Runoob","Taobao"]
# for site in sites:
#   if site == 'Runoob':
#     print('Runoob')
#     continue
#   print("round %s" %site)
# else:
#   print("no data")
# print("done")  

prime = int(input('input num to check is prime number '))
if prime > 0:
  if prime == 1:
    print('1 is not prime')  
  else:  
    for num in range(2, prime):
      if( prime % num == 0):
        print('%d is not prime, it can be exact by %d' %(prime, num))
        break
    else:
      print('%d is prime' %prime)  
else:
  print('Error, input must > 0')