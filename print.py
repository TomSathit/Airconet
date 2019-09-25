import sys  # getsizeof

x=y=z=50

a,b = 300,400

print('sathit')
print(215853)
print('x=',x,y,z)
print('a =',a)
print('b =',b)

a,b =b,a  #สลับตัวแปร

print('a =',a)
print('b =',b)
print(a,b)

k=5.65
print('num = %d' %k)

print(type(k))

print('k have size =',sys.getsizeof(k))
