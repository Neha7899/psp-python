"""homogenous set example"""
a={10,20,30,40,50}
print(a)#op={50, 20, 40, 10, 30}-unordered

a={10,20,30,40,50,10,20,30}
print(a)#op={50, 20, 40, 10, 30}-removes dupicates by itself if passed

"""heterogenous set example"""
b={10,13.4,2+3j,'john',True}
print(b)#op={True, 'john', 10, (2+3j), 13.4}-unordered

b={10,13.4,2+3j,'john',True,10,True,2+3j}
print(b)#op={True, 'john', 10, (2+3j), 13.4}-removes duplicates by itself if passed

print(type(b))#op=<class 'set'>


# z={10,31,4,5+6j,[10,20,30],'abraham',False}
# print(z)#op=TypeError: unhashable type: 'list'


# z={10,31,4,5+6j,{10,20,30},'abraham',False}
# print(z)#op=TypeError: unhashable type: 'set'

a='a'
print(type(a))