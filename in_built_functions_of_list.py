l=[10,20,30,40,50,60,70,80,90,100]
print(l)
print(id(l))
print(type(l))
print(len(l))


#append()
print(l.append(1))


#extend()
print(l.extend([2,3]))


#insert()
print(l.insert(1,'ben'))



#remove()
print(l.remove(1))


#pop()
print(l.pop(2))


#clear()
print(l.clear())



l=[10,20,30,40,50,60,70,80,90,100]

#index()
print(l.index('20'))


#count()
print(l.count(30))



#sort()
print(l.sort(key=len,reverse=True))


#reverse()
print(l.reverse())


#copy()
m=copy(l)
print(m)