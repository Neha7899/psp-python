d={'a':10,'b':20,'c':30,'d':40,'e':50}
print(d)
print(id(d))
print(type(d))
print(len(d))


#update()

e={'f':1,'g':2,'i':3,'j':4,'k':5}

# x=d.update({'a':1,'b':2})
# print(x)


#get()
print(d.get('a'))


#setdefault()
print(d.setdefault('a',-1))
print(d)


#fromkeys()
e=dict.fromkeys(['a','b'],10)
print(e)


#pop()
print(d.pop('a',-1))


#popitem()
print(d.popitem())


#clear()
print(d.clear())



d={'a':10,'b':20,'c':30,'d':40,'e':50}


#items()
print(d.items())


#keys()
print(d.keys())


#values()
print(d.values())



#copy()
x=d.copy()
print(x)