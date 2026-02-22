#WAP to check if a number is positive
# n=int(input("enter a number:"))
# if n>=0:
#     print("the entered number is positive")

#WAP to check if a number is negative or positive using if-else
# n=int(input("enter a number:"))
# if n>=0:
#     print("the entered number is positive")
# else:
#     print("the entered number is negative")


#WAP to check whether a number is even or odd
# n=int(input("enter a number:"))
# if n%2==0:
#     print("even number")
# else:
#     print("odd number")


#WAP to check if a person is eligible to vote(age>=18)
# age=int(input("enter your age:"))
# if age>=18:
#     print("eligible to vote")
# else:
#     print("not eligible")

#WAP to check if a number is divisible by 5
# n=int(input("enter a number:"))
# if n%5==0:
#     print("divisible by 5")
# else:
#     print("not divisible by 5")


#WAP to compare two numbers and print the greater number
# num1=int(input("enter a number:"))
# num2=int(input("enter a number:"))
# if num1>num2:
#     print("greater number is:",num1)
#elif num2>num1:
#     print("greater number is:",num2)
# else:
#     print("both are equal")


#WAP to check whether a given character is a vowel or not
# char=input("enter a character:")
# vowels=('a','e','i','o','u','A','E','I','O','U')
# if char in vowels:    #or if char in ('a','e','i','o','u','A','E','I','O','U')/'AEIOUaeiou'
#     print("character is vowel")
# else:
#     print("not a vowel")


#WAP to check if a student has passed (marks>=40) or failed
# marks=int(input("enter the marks:"))
# if marks>=40:
#     print("student has passed")
# else:
#     print("student has failed")


#WAP to check whether a number is zero,postive or negative
# n=int(input("enter a number:"))
# if n==0:
#     print("it is a zero")
# elif n>0:
#     print("it is positive number")
# else:
#     print("it is negative number")

#WAP to find the largest of two numbers using if-else
# num1=int(input("enter the first number:"))
# num2=int(input("enter the second number:"))
# if num1>num2:
#     print("largest number is:",num1)
# else:
#     print("largest number is:",num2)


#WAP to find relation between two integers(greater,lesser or equal)
# num1=int(input("enter the first number:"))
# num2=int(input("enter the second number:"))
# if num1>num2:print(num1,"is greater than",num2)
# elif num1<num2:print(num1,"lesser than",num2)
# else:print(num1,"is equal to",num2)




#WAP to check the given integer is single,double,triple or more than 3 digit
# n=int(input("enter the number:"))
# if 0<=n<=9:
#     print("single digit")
# elif 10<=n<=99:
#     print("two digit")
# elif 100<=n<=999:
#     print("three digit")
# else:
#     print("more than 3-digit")


#WAP to check whether the character is uppercase,lowercase,number or special symbol
# ch=input("enter the character:")
# if 'A'<=ch<='Z':
#     print("Uppercase")
# elif 'a'<=ch<='z':
#     print("Lowercase")
# elif '0'<=ch<='9':
#     print("Numbers")
# else:
#     print("Special Characters")


#WAP to find the greatest among 4 numbers
# num1=int(input("enter a mumber:"))
# num2=int(input("enter a mumber:"))
# num3=int(input("enter a mumber:"))
# num4=int(input("enter a mumber:"))



#WAP to check whether the entered character is a vowel or not
# ch=input("enter the character:")
# if ch in 'AEIOUaeiou':
#     print("entered character is vowel")
# else:
#     print("not a vowel")

# ch=eval(input("enter the character:"))
# if type(ch)==str:
#     if ch in "AEIOUaeiou":
#         print("vowel")
#     else:
#         print("consonant")
# else:
#     print("not a string")

#WAP to create Mail and Password validator
# id="john999@gmail.com"
# password="john999"
# userid=input("enter the mail:")
# if id==userid:
#     print("mail id is correct")
#     userpassword=input("enter the password:")
#     if password==userpassword:
#         print("login successful")
#     else:
#         print("password incorrect")
# else:
#     print("incorrect mail id.login failed.try again")


#WAP to check whether the last data of a list is string if yes then check if it is a pallindrome(nayan,malayalam,mom,madam,dad)
# list=eval(input("enter the list:"))
# if type(list[-1])==str:
#     if list[-1]==list[-1][::-1]:
#         print("it's a pallindrome")
#     else:
#         print("not a pallindrome")
# else:
#     print("not a string")
