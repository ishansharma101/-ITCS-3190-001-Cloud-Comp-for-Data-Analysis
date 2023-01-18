from collections import OrderedDict 

def removeDuplicates(list): 

     list = [*set(list)]
     return list


print(removeDuplicates([1,2,3,4,2,5,2,3,4]))

