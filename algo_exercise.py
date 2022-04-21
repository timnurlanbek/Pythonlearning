from ctypes.wintypes import tagRECT
from email.errors import StartBoundaryNotFoundDefect
import numbers
from re import I


# given a list of numbers, find first two indeces that make total equal to target
# my_list = [3,2,4,-10,5,7,6,11]

# target = 9

# output:[0,6]

# def two_sum(lst,target):

#     outer loop:;loops over elements one by one with i
        
#         inner loop, loops elementes one by one with j
#             if i+j==target:
#                 return[i,j]



# my_list = [3,2,4,-10,5,7,6,11]
# two_sum()





# def two_sum(lst,target):
#     new_list=0
#     for i in range(len(lst)):
#         for j in lst:
#             if i+j == target:
#                 return[i,j,lst.index(i),lst.index(j)]
#     return "failed to find anyone"
        
        
# my_list = [3,2,4,-10,5,7,6,11]
# print(two_sum(my_list,9))

dnfmsdnfmd,StartBoundaryNotFoundDefect
fdsnnfmds




# def two_sum(lst,target):
#     new_list=0
#     for i in range(len(lst)):
#         for j in range (i+1,len(lst)):
#             if lst[i]+lst[j] == target:
#                 return [lst[i],lst[j]]
#     return "failed"
        
        
# my_list = [3,2,4,-10,5,7,6,11]
# print(two_sum(my_list,9))
mesage = """never compare 
your self with another person. You never know what their 


Two sum leet code"""


# given string of word , convert it to list of words
my_string = "hi hello how are you doing?"
# exp output : ["hi", "how", "are", "you", "doing?"]
print(list(my_string))

def split_txt(str):
    #return str.split(" ")
    new_lst=[]
    temp_string=""
    for i in str:
        if i==" ":
            new_lst.append(temp_string)
            temp_string=' '
        else:
            temp_string=temp_string+i
    new_lst.append(temp_string)
    return new_lst

my_string="hi hello how are you doing?"
print(split_txt(my_string))

# given a string 
# find first no n repeating character 

# string = "market models are" {"m":2, }

# output: K 
def non_repeating(string):
    dictionary={}
    for i in string:
        if i in dictionary:
            dictionary[i]+=1
        else:
            dictionary[i]=1
    for i in dictionary:
        if dictionary[i]==1:
            return i
print(non_repeating("market models are"))