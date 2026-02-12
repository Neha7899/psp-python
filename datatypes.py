#SINGLE-VALUED DATATYPES
#NUMERIC DATATYPES
#1.INTEGER DATATYPE(int)
a=10
print(a) #op=10
print(type(a))  #op=<class 'int'>
print(id(a))   #op=140723140117704
print(bool(a))  #op=True-because it is a non-default value of integer datatype

x=0
print(x)   #op=0
print(type(x))  #op=<class 'int'>
print(id(x))   #op=140723140117384
print(bool(x))  #op=False-because it is default value of integer datatype

#2.FLOAT DATATYPE(float)
a=15.3
print(a) #op=15.3
print(type(a))  #op=<class 'float'>
print(id(a))   #op=1953497324176
print(bool(a))  #op=True-because it is a non-default value of float datatype

x=0.0
print(x)   #op=0.0
print(type(x))  #op=<class 'float'>
print(id(x))   #op=1624728967664
print(bool(x))  #op=False-because it is default value of float datatype

#3.COMPLEX DATATYPE(complex)
a=3+4J
print(a) #op=(3+4j)
print(type(a))  #op=<class 'complex'>
print(id(a))   #op=1461858567824
print(bool(a))  #op=True-because it is a non-default value of complex datatype

x=0j
print(x)   #op=0j
print(type(x))  #op=<class 'complex'>
print(id(x))   #op=2559380199952
print(bool(x))  #op=False-because it is default value of complex datatype

#BOOLEAN DATATYPE(bool)
a=True
print(a) #op=True
print(type(a))  #op=<class 'bool'>
print(id(a))   #op=140723139232176
print(bool(a))  #op=True-because it is a non-default value of boolean datatype

x=False
print(x)   #op=False
print(type(x))  #op=<class 'bool'>
print(id(x))   #op=140723139232176
print(bool(x))  #op=False-because it is default value of boolean datatype




#MULTI-VALUED DATATYPES
#1.STRING DATATYPE(str)
a='john'
print(a) #op=john
print(type(a))  #op=<class 'str'>
print(id(a))   #op=2164871939152
print(bool(a))  #op=True-because it is a non-default value of string datatype

x=''
print(x)   #op=
print(type(x))  #op=<class 'str'>
print(id(x))   #op=140723140138688
print(bool(x))  #op=False-because it is default value of string datatype


#2.LIST DATATYPE(list)
a=[10,20,'john',True,3.14]
print(a) #op=[10, 20, 'john', True, 3.14]
print(type(a))  #op=<class 'list'>
print(id(a))   #op=1700594540736
print(bool(a))  #op=True-because it is a non-default value of list datatype

x=[]
print(x)   #op=[]
print(type(x))  #op=<class 'list'>
print(id(x))   #op=1822023763136
print(bool(x))  #op=False-because it is default value of list datatype


#3.TUPLE DATATYPE(tuple)
a=(1,2,3,4,5)
print(a) #op=(1, 2, 3, 4, 5)
print(type(a))  #op=<class 'tuple'>
print(id(a))   #op=1727287695280
print(bool(a))  #op=True-because it is a non-default value of tuple datatype



x=()
print(x)   #op=()
print(type(x))  #op=<class 'tuple'>
print(id(x))   #op=140723140191680
print(bool(x))  #op=False-because it is default value of tuple datatype


#4.SET DATATYPE(set)
a={1,2,3,1,3}
print(a) #op={1,2,3}
print(type(a))  #op=<class 'set'>
print(id(a))   #op=2167038083808
print(bool(a))  #op=True-because it is a non-default value of set datatype

x=set()
print(x)   #op=set()
print(type(x))  #op=<class 'set'>
print(id(x))   #op=2971724896448
print(bool(x))  #op=False-because it is default value of set datatype


#5.DICTIONARY DATATYPE(dict)
a={'a':1,'b':2,'c':3}
print(a) #op={'a': 1, 'b': 2, 'c': 3}
print(type(a))  #op=<class 'dict'>
print(id(a))   #op=1598765000256
print(bool(a))  #op=True-because it is a non-default value of dictionary datatype


x={}
print(x)   #op={}
print(type(x))  #op=<class 'dict'>
print(id(x))   #op=2128902745280
print(bool(x))  #op=False-because it is default value of dictionary datatype
