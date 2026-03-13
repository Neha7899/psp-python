# def reg(name,phno,email,altphno,altemail):
#     print('name is',name)
#     print('phno is',phno)
#     print('email is',email)
#     print('altphno is',altphno)
#     print('atlemail is',altemail)
# reg('amith',1234567890,'abc@gmail.com')
#op=error(values given are not equal to the arguments or 2 positional arguments are missing)


# def reg(name,phno,email,altphno=None,altemail=''):
#     print('name is',name)
#     print('phno is',phno)
#     print('email is',email)
#     print('altphno is',altphno)
#     print('atlemail is',altemail)
# reg('amith',1234567890,'abc@gmail.com')


#WAP to add minimum two numbers and maximum 5 numbers
# def add(a,b,c=0,d=0,e=0): #or def add(a,b,c=0,d=0,e=0)
#     sum=(a+b+c+d+e)
#     print(sum)
# add(1,2,3,4,5)#can give min 2 to max 5 values

#or

# def add(a,b,c=0,d=0,e=0):
#     return a+b+c+d+e
# print(add(1,2,3,4,5))#can give min 2 to max 5 values


#WAP to find the product of minimum 3 numbers and maximum 5 numbers
# def mul(a,b,c,d=1,e=1):
#     return a*b*c*d*e
# print(mul(1,2,3))  #can take min 3 to max 5 values

#or

# def mul(a,b,c,d=1,e=1):
#     product=a*b*c*d*e
#     print(product)
# mul(1,2,3,4,5)


#or 

# def prod(a,b,c,d=1,e=1):
#     # print(a*b*c*d*e)
#     return a*b*c*d*e
# print(prod(2,3,4))


#WAP to extract float numbers from tuple(output should be in the form of tuple only)
# def ext_float(a):
#     num=()
#     for i in a:
#         if type(i)==float:
#             num=i
#             i=i+1
#         print(num)
# ext_float(eval(input("enter the tuple elements:")))




#WAP to find the sum of individual digits in a given integer(ex:23->2+3=5)
def sum_of_individuals(a):
    sum=0
    for i in a:
        if type(a)==int:
            


