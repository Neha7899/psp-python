#while looping statement


#printing Hello for 5 times using while looping statement
# i=0                   #initialization
# while i<5:            #while condition:
#     print("Hello")    #    statement block
#     i+=1              #    updation 


#WAP to print "Hello,World" for 10 times
# i=0
# while i<10:
#     print("Hello,World")
#     i+=1


#WAP to print values from 1 to 10
# i=1
# while i<=10:
#     print(i)
#     i+=1

#WAP to print values from 10 to 1
# i=10
# while i>=1:
#     print(i)
#     i-=1

#WAP to print even numbers between 1 to 20
# i=1
# while i<=20:
#     if i%2==0:
#         print(i)
#     i+=1    
    

#WAP to print the sum of n natural numbers 
# n=int(input("Enter the number:"))
# i=1
# sum=0
# while i<=n:
#     sum+=i
#     i+=1
# print(sum)




#for looping statement

#sample program

# for i in range(1,11,1):
#     print(i)


# for i in 'PYTHON':
#     print(i)


# for i in [10,20,30,40,50]:
#     print(i)


#WAP to find the length of a string without using len()
# s=input("enter the string:")
# count=0
# for i in s:
#     count+=1
# print(count)




#ASSIGNMENT QUESTIONS
#FOR LOOP QUESTIONS

#WAP to find the length of the list
# l=eval(input("enter the list:"))
# count=0
# for i in l:
#     count+=1
# print(count)


#WAP to extract the vowels from the given string
# s=input("enter the string:")
# c=''
# count=0
# for i in s:
#     if i in 'AEIOUaeiou':
#         c+=i
#         count+=1
# print(c,count,sep=',')


#WAP to reverse a string without slicing
# s = input("Enter a string: ")
# rev = ""
# for i in s:
#     rev = i + rev
# print("Reversed string:", rev)






#WAP to print a table of n number
# n=int(input('enter a number:'))
# for i in range(1,11):
#     print(f"{n}x{i}={n*i}")#f means formatted string and {} are mandatory inside the f










#WHILE LOOP QUESTIONS

#WAP to reverse the number without using typecasting
# num = int(input("Enter a number: "))
# rev = 0
# while num > 0:
#     digit = num % 10
#     rev = rev * 10 + digit
#     num = num // 10
# print("Reversed number:", rev)


#WAP to print the product of individual digit of the number(24->2*4=8)
# num = int(input("Enter a number: "))
# product = 1
# while num > 0:
#     digit = num % 10
#     product = product * digit
#     num = num // 10
# print("Product of digits:", product)



#WAP to print the sum of individual digit of the number(24->2+4=6)
# num = int(input("Enter a number: "))
# sum = 0
# while num > 0:
#     digit = num % 10
#     sum = sum+digit
#     num = num // 10
# print("sum of digits:",sum)



#while loop questions
#WAP to print
#1.first 10 even numbers
# i=1
# while i<=20:
#     if i%2==0:
#         print(i)
#     i=i+1


#2.first 10 odd numbers
# i=1
# while i<=20:
#     if i%2!=0:#or if i<%2==1
#         print(i)
#     i+=1


#3.first 10 natural numbers(1 to 10)
# i=1
# while i<=10:
#     print(i)
#     i+=1


#4.first 10 whole numbers(0 to 9)
# i=0
# while i<10:
#     print(i)
#     i+=1


#5.WAP to print first 10 integers and their squares using while loop
# i=0
# while i<10:
#     print(i, i**2) #or print(i, i*i)
#     i+=1



#6.write while loop statement to print the following series:10,20,30,......,300
# i=0
# while i<300:
#     print(i+10)
#     i+=10


# i=1
# while i<=300:
#     if i%10==0:
#         print(i)
#     i+=1    


#7.write a while loop statement to print the following series:105,98,91........,7
# i=112
# while i<=112:
#     print(i-7)
#     i-=7
#     if i<=7:
#         break


# i=105
# while i>=7:
#     if i%7==0:
#         print(i)
#     i-=1


#8.write a program to print the first 10 natural number in reverse 
# i=10
# while i<=10:
#     print(i)
#     i-=1
#     if i<=0: # if i==0:
#         break


# i=10 
# while i>=1:
#     print(i)
#     i-=1




#9.wap to print sum of first 10 natural numbers
# i=0
# sum=0
# while i<=10:
#     sum+=i
#     i+=1
# print(sum)



#10.wap to print sum of first 10 even numbers
# i=1
# sum=0
# while i<=20:
#     if i%2==0:
#         sum+=i
#     i+=1
# print(sum)




#for loop questions

#1.accept an integer and print hello world n times
# n=int(input("enter the number:"))
# for n in range(0,n,1):
#     print("hello,world")


#2.print natural number up to n
# n=int(input("enter a number:"))
# for i in range(1,n+1,1):
#     print(i)



#3.reverse for loop. print n to 1
# n=int(input("enter a number:"))
# for i in range(n,0,-1):
#     print(i)






