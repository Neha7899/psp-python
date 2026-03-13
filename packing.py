#packing

#1.single or tuple packing

#sample programs

# def pack(*a):    # '*' means it stores multiple values in the given variable
#     print(type(a))
#     print(a)
# pack(10,20,30,40,50)
#op=<class 'tuple'>
#(10, 20, 30, 40, 50)

# def pack(a):   
#     print(type(a))
#     print(a)
# pack(10)
#op=<class 'int'>
#10

# def pack(*a):   
#      print(type(a))
#      print(a)
# pack()
#op=<class 'tuple'>
#()



#2.double or dictionary packing

#sample programs

# def pack(**a):
#     print(type(a))
#     print(a)
# pack(a=1,b=2,c=3)
#op=<class 'dict'>
#{'a': 1, 'b': 2, 'c': 3}

# def pack(a):
#     print(type(a))
#     print(a)
# pack(a=1)
#op=<class 'int'>
#1

# def pack(**a):
#     print(type(a))
#     print(a)
# pack(a=1)
#op=<class 'dict'>
#{'a': 1}

# def pack(**a):
#     print(type(a))
#     print(a)
# pack()
#op=<class 'dict'>
#{}



#passing both tuple and dict at a time
#positional arguments follows keyword arguments
# def pack(*a,**b):
#     print(type(a))
#     print(a)
#     print(type(b))
#     print(b)
# pack(10,20,30,a=1,b=2,c=3)
#op=<class 'tuple'>
# (10, 20, 30)
# <class 'dict'>
# {'a': 1, 'b': 2, 'c': 3}


