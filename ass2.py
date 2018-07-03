set1= {1,2,5,4,3}
set2=set([5,6,7,8,9])
print("----Set Operations using Opearators----")
print("Contents of number set 1 are::")                      
print (set1)
print("Contents of number set 2 are::")                      
print (set2)

print("set1-set2",set1-set2)
print("Union::",set1|set2)
print("Intesection::",set1&set2)
print("Symmetric differance::",set1^set2)


print("----Set Operations using functions----")
basket1= {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
basket2= {'mango', 'orange', 'grapes', 'pear', 'straberry',}
print("Contents of basket 1 set are::")                      
print (basket1)
print("Contents of basket 2 set are::")                      
print (basket2)

print("Check apple available in basket1 ::",'apple' in basket1)
print("set1-set2",basket1-basket2)
print("Union::",basket1.union(basket2))
print("Intesection::",basket1.intersection(basket2))
print("Symmetric differance::",basket1.symmetric_difference(basket2))

#OUTPUT::
==================== RESTART: /home/unix/Desktop/ass2.py ====================
----Set Operations using Opearators----
Contents of number set 1 are::
{1, 2, 3, 4, 5}
Contents of number set 2 are::
{8, 9, 5, 6, 7}
set1-set2 {1, 2, 3, 4}
Union:: {1, 2, 3, 4, 5, 6, 7, 8, 9}
Intesection:: {5}
Symmetric differance:: {1, 2, 3, 4, 6, 7, 8, 9}
----Set Operations using functions----
Contents of basket 1 set are::
{'apple', 'orange', 'banana', 'pear'}
Contents of basket 2 set are::
{'straberry', 'grapes', 'mango', 'orange', 'pear'}
Check apple available in basket1 :: True
set1-set2 {'apple', 'banana'}
Union:: {'apple', 'straberry', 'orange', 'mango', 'pear', 'banana', 'grapes'}
Intesection:: {'orange', 'pear'}
Symmetric differance:: {'straberry', 'apple', 'mango', 'banana', 'grapes'}
>>> 

