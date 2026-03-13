s={10,20,30,40,50}
print(s)
print(id(s))
print(type(s))
print(len(s))


#add()
s.add(60)
print(s)


#update()
s.update([1,2])
print(s)


#remove()
s.remove(10)
print(s)



#pop()
s.pop()
print(s)


#discard()
s.discard(2)
print(s)


#clear()
s.clear()
print(s)


x={10,20,30,40,50}
y={40,50,60,70,80}


#union()
z=x.union(y)
print(z)



#intersection()
z=x.intersection(y)
print(z)



#difference()
z=x.difference(y)
print(z)



#symmetric_difference()
z=x.symmetric_difference(y)
print(z)