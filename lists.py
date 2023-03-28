#part 2
my_list=[]
my_list.append(76)
my_list.append(92.3)
my_list.append('hello')
other_list=[True,4,76]
my_list=my_list+other_list
#part 3
my_list.append("apple")
my_list.append(76)
my_list.insert(3, "cat")
index=my_list.index("hello")
count=my_list.count(76)
remove=my_list.remove(76)
pop=my_list.pop(3)
print(my_list)
#part 4
'''def sum_of_squares(lst):
  sum_= 0
  for e in lst:
      product=e*e
      sum_=sum_ + product
  return sum_

lst = [2, 3, 4]
print(sum_of_squares(lst))'''
import random
xs = []
for i in range(3):
    xs.append(random.randint(0,100))
def sum_of_squares(xs):
    sum_=0
    for i in (xs):
        squared = i * i
        sum_ = sum_ + squared 
    return sum_
print (sum_of_squares(xs))
