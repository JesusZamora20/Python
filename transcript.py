#list comprehension

list1 = [0,1,2,3,4,5,6,7]
listC = [i for i in range(7)]
print(listC)

listC = [i + 1 for i in range(7)]
print(listC)

listC = [i * 2 for i in range(7)]
print(listC)

def sumfive(number):
  return number + 5

listC = [sumfive(i) for i in range(7)]
print(listC)
