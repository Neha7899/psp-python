#Types of user-defined functions


#1.function without argument and without return value

#skeleton
# def add():
#     a=int(input())
#     b=int(input())
#     print(a+b)
# add()


#WAP to find the sum of two integers

# def add():
#     a=int(input("enter the number:"))
#     b=int(input("enter the numnber:"))
#     print(a+b)
# add()



#WAP to convert the string into uppercase
# def con_upper():
#     s=input("enter a string:")
#     print(s.upper())
# con_upper()


#WAP to count the number of occurences of given character in a string
# def count_char():
#     s=input("enter the string:")
#     print(s.count('a'))
# count_char()

# taking the character from the user and finding the number of occurences of it
# def count_char():
#     s=input("enter the string:")
#     ch=input("enter a character:")
#     print(s.count(ch))
# count_char()





#2.function with arguments and without return value

#WAP to find the sum of 2 numbers
# def add(a,b):
#     print(a+b)
# add(10,20)


#WAP to extract string from the list which are palindrome
# def ex_pal(l):
#     out=[]
#     for i in l:
#         if type(i)==str:
#             if i==i[::-1]:
#                 out.append(i)
#     print(out)
# ex_pal(eval(input("enter the list:")))


#WAP to find the greatest among three numbers
# def great_num(m,n,o):
#     for i in (m,n,o):
#         if m>=n and m>=o:
#             print(m)
#         elif n>=m and n>=o:
#             print(n)
#         else:
#             print(o)
# great_num(10,20,30)


# def gta3(a,b,c):
#      if a>b and a>c:print(a,"is greater")
#      elif b>a and b>c:print(b,'is greater')
#      else:print(c,'is greater')
# gta3(10,20,30)



#WAP to concatenate two list collections without using + operator
# def concatenate_lists(list1, list2):
#     for item in list2:
#         list1.append(item)
#     print("Concatenated List:", list1)
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# concatenate_lists(list1, list2)


# def concatenate_lists(list1, list2):
#     list1.extend(list2)
#     print("Concatenated List:", list1)
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# concatenate_lists(list1, list2)



#3.function without arguments and with return value

#WAP to perform arithmetic operations
# def ar_op():
#     a=int(input('enter the value:'))
#     b=int(input('enter the value:'))
#     return(a+b,a-b,a*b,a/b,a//b,a%b,a**b)
# print(ar_op())


#WAP to perform relational operations
# def rl_op():
#     a=int(input('enter the value:'))
#     b=int(input('enter the value:'))
#     return(a==b,a!=b,a>b,a<b,a>=b,a<=b)
# print(rl_op())


#WAP to find the sum of integers present inside a given set
# def sum_int():
#     s=eval(input("enter the set elements:"))
#     sum=0
#     for i in s:
#         if type(i)==int:
#             sum+=i
#     return sum
# print(sum_int())




#4.function with arguments and with return values

#WAP to perform relational operators
# def rel_op(a,b):
#     return a==b,a!=b,a<b,a>b,a<=b,a>=b
# print(rel_op(20,50))


#WAP to extract negative integers from the list
# def neg_int(num):
#     out=[]
#     for i in num:
#         if type(i)==int:
#             if i<0:
#                 out.append(i)
#     return out
# print(neg_int(eval(input("enter the list elements:"))))
    

