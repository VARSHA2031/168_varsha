# # print(this is my first programme)
# # print(Hello World)
# # # print(18)

# # a = varsha
# # print(a)
# # print(type(a))
# # b = 12
# # c = 12.2
# # d = True

# # print(b) 
# # print(c)
# # print(d)


# #CHECKING A DATATYPE
# # #FLAT CASE = all alphabet in small letters 
# # myname = yash
# # #snake case = there is a underscore btw two words
# # my_name_class = xyz
# # #cmael case = the second letter is a upercase .
# # myname = xyz
# # #pascal case = every first letter is in capital letters.
# # MyName = xyz


# my_class = complex(1,3)
# print(type(my_class))
# x = 12
# print(type(x))
# x = you are champion in your field.
# print(type(x))
# x = 12.26
# print(type(x))

# #DATA TYPE IN PYTHON



# #2seaquence
# # b1 = string () it's always 
# # x = 12
# # print(type(x))
# # x = you are champion in your field.
# # print(type(x))
# # x = 12.26
# # print(type(x))
# # a3 = complex(3,5)
# # print(type(a3))


# # my_list = [1,35,65,you are not performing well]
# # print(my_list)
# # print(type(my_list))
# # my_list.append(1)
# # print(my_list)
# # my_list.insert(3,45)
# # print(my_list)
# b2 = [1,2,3,yash]
# print(type(b2))
# b3 = (1,2,3,yash)
# print(type(b3))
# my_dictionary = {'name'  rishab, 'age'26, 'city''dehradun'}
# print(type(my_dictionary))

# my_list = [1,35,65,you are not performing well]
# print(my_list)
# # removing elements in list 
# my_list.remove(65) #remove by element
# my_list.pop() #last element
# del my_list[0] #by indexing

# my_list = [1,35,65,you are not performing well]
# my_list.remove(65) 
# print(my_list)

# my_list = [1,35,65,you are not performing well]
# del my_list[2]
# print(my_list)

# my_list = [1,35,65,you are not performing well]
# my_list.remove(65)
# print(my_list)

# my_list = [1,35,65,you are not performing well]
# print(len(my_list))

# my_list = [1,35,65,65,66,80] #to find minimum value in list for example 1 is the min value
# print(min(my_list)) 

# my_list = [1,35,65,65,66,80] # to find the max value in list example 80
# print(max(my_list))

# age = int(input(enter your age))
# if age  13
#     print(you are a child)
# elif age  20
#     print(you are a teen ager)
# elif age  60
#     print(you are an adult)
# else
#     print(you are a senior citizen)

# #star pyramids in python code
# rows = int(input(Enter number of rows ))
# for i in range(1, rows + 1)
#     print(   (rows - i), end=)
#     print(  (2  i - 1))

# #TUPLE - immutable 
# my_tuple = (1,2,3)#simple tuple
# my_tuple = (2,hello,3) #mixed tuple
# my_tuple = (5) # single tuple
# print(my_tuple)
# elif light == yellow
#     print(get ready)
# elif light == green
#     print(go)
# else
#     print(invalid light colour!)

# #loop 
# A loop executes a block of code multiple times until a condition is false or a sequence is finished.
# #for loop
# used when we know how many times to run(works with list, tuple, string, dict, range).
# for i in range(5)
#     print(hello, i)

# # 2. while loop 
#  used when we don't know exact repetations; runs until condition is false.
# count = 1
# while count = 5
#     print(hello, count) 
#     count += 1

# 3. loop control
 #break - exit loop immediately
 #continue - skip current iteration
 #pass - do nothing (placeholder)
# for i in range(1,6)
#     if i == 3
#         continue 
#     if i == 5
# #         break
# #     print(i)

# # # 4. nested loops 
# # loops inside another loops.
# '''for i in range(2)
#     for j in range(3)
#          print(i =, i, j =, j)'''

# #q1. Print number from 1 to 10 using a for loop
# '''i=0
# for i in range(1,11)
#     print(i)

# #print number number from 10 to 1 using a while loop
# i=10
# while(i=1)
#     print(i)
#     i-=1

# #print the multiplecation table 5 using a for loop
# i=0
# for i in range(1,11)
#     print(f'5x{i}',5i)

# #program to print only even number
# i=0
# while(i=20)
#     if(i%2==0)
#         print(i)
#     i+=1

# #pattern using a nested loop
# i,j=0,1
# for i in range(1)
#     for j in range(1,10)
#         print(' 'j)
#         j+=1'''

# import pandas as pd
# '''df=pd.DataFrame([1,2,3],columns=['columnName'])
# print(df)

# abc= {
#     'name'[ 'ansha','suman'],
#     'age'  [20,18],
#     'salary'  [10000,20000000]
# }
# df=pd.DataFrame(abc)
# print(df)
# print(df.head())
# print(df.tail())
# print(df.shape())
# print(df.columns())
# print(df.rename(columns={'salary''payment'}))
# print(df.describe())'''
# co={
#     'name' ['yas','shi','anil','sunil','suman','dempi','ardna','as','pas','kas'],
#     'employes_id' [1000,1004,1003,10005,1005,1006,1007,1008,1009,100010],
#     'age' [10,12,13,14,15,20,90,320,20,40],
#     'salary' [1000000,12,2000,3000,3000,3000,5000,400,2000,1]
# }
# data = pd.DataFrame(co)
# print(data)