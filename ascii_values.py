#ord()-ordinal
#syntax=ord('character')

print(ord("a"))
#op=97



print(ord('A'))
#op=65


print(ord('1'))
#op=49

print(ord('0'))
#op=48

print(ord('$'))
#op=36



#chr()-character
#syntax=chr(ascii value)

print(chr(100))
#op=d

print(chr(64))
#op=@


print(chr(33))
#op=!


print(chr(65))
#op=A



#conversion of uppercase to lowercase
#syntax=chr(ord('UPPERCASE_CHAR')+32)

print(chr(ord("A")+32))
#op=a


print(chr(ord('M')+32))
#op=m



#conversion of lowercase to uppercase
#syntax=chr(ord('LOWERCASE_CHAR')-32)

print(chr(ord('a')-32))
#op=A

print(chr(ord('x')-32))
#op=X

print(chr(ord('f')-32))
#op=F