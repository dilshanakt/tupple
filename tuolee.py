tuple=(0,1,2,3,4,5,6,7,8,9)
len=len(tuple)
print(len)

print(tuple[:len])
print(tuple[3:6])
print(tuple[6:9])
print(tuple[2:7])
print(tuple.count(5))
print(tuple.index(1))

fruits=("apple","banana","chery","guava","mango","pinepple")
a,*b,c=fruits
print(a)
print(b)
print(c)
