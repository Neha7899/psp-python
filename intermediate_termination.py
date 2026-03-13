#break 

#1.WAP to find the first multiple of 5 between 1 and 20 and break the loop
# for i in range(1,21):
#     if i%5==0:
#         print(i)
#         break



#2.loop through a list of names and stop if the name "rahul" appears
# n=['neha','srishanth','mamatha','rahul','keerthy','uma']
# for i in n:
#     if i=='rahul':
#         break
#     print(i)



#3.print characters of a word but stop if you find the letter 'o'
# c='aeiou'
# for i in c:
#     if i=='o':
#         break
#     print(i)



#4.WAP that keeps asking for a password until the user enters "1234",then break
# while True:
#     password=input("enter the password:")
#     if password=='1234':
#         print('correct password')
#         break
#     else:
#         print("incorrect password")




#continue

#1.print numbers from 1 to 10,skipping even numbers
# for i in range(1,11):
#     if i%2==0:
#         continue
#     print(i)        



#2.print numbers from 1 to 20,skipping multiples of 3
# for i in range(1,21):
#     if i%3==0:
#         continue
#     print(i)



#3.loop through a string and print all chararcters except 'a'
# s='chair'
# for i in s:
#     if i=="a":
#         continue
#     print(i)



#4.loop from 1 to 10 but skip printing number 5
# for i in range(1,11):
#     if i==5:
#         continue
#     print(i)



#5.print only odd numbers from a list [1,2,3,4,5,6,7,8,9,10] using continue
# l=[1,2,3,4,5,6,7,8,9,10]
# for i in l:
#     if i%2==0:
#         continue
#     print(i)




#pass

#1.write a loop from 1 to 5,but do nothing when the number is 3
# for i in range(1,6):
#     if i==3:
#         pass
#     print(i)


#2.loop through letters of 'python',and if the letter is 't',just use pass(do nothing)
# a='python'
# for i in a:
#     if i=='t':
#         pass
#     print(i)



#3.WAP that checks numbers 1-10 but for number 7,just pass (ignore it)
# for i in range(1,11):
#     if i==7:
#         pass
#     print(i)