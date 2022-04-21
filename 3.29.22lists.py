# LISTS
# ordered collection of different data types, mutable
# my_list = [10,45,5,True, "good morning", {1,2,3,4}, "goodbye"]
# print(len(my_list))
# print(type(my_list))


# for element in range (len(my_list) -1,-1,-1): # 0 - len(my_list)
    # print(my_list[element])



# salary = [123123,41232,[12,30,["hi",[40,50,[100]]]]]
# print(type(salary))
# print("length of salary is :" , len(salary))
# a= [10,[20,30]]
#a[-1][0] >>20
# print(salary[-1][2][-1][-1][0])

#print integer 100 from salary list

# pirnt legth of [40,50,[100]] substring from salary list
# print(len(salary[-1][-1][1]))
# print length of [12.30.["hi"]] ... from salary list
# print(len(salary[-1]))

# matrix = [[2,3,4],[5,6,7]]
# sum=0
# for i in matrix:
#     for j in i:
#         sum=sum+j
#         # print(j)
# print(sum)


# list_of_numbers = [10,20,30,15,20,40,50]
# get sum of list_of_numbers
#calculate average of list_of_numbers
#find the element in the middle
# tot=0
# for i in list_of_numbers:
#     sum=sum+1
#     tot+=i
# print(tot,"total")
# print(tot/len(list_of_numbers),"average")
# print(list_of_numbers[len(list_of_numbers)//2])


# a= [-9,2,1,34,352]
# a.append(999)
# a.insert(0,234)
# a.insert(5,"hello")
# a.sort()
# print(a)
# a.reverse()
# a.remove(2)
# print(a.index("hello"))
# print(a)

b=[100,20,30,40]
new_list = []
for i in range(len(b)-1,-1,-1):
    new_list.append(b[i])
print(new_list)

def reverse_list(lst):
    new_list=[]
    for i in range(len(lst)-1,-1,-1):
        new_list.append(lst[i])

    return new_list
print(reverse_list([90,123,"asd","hi",True,-90]))

