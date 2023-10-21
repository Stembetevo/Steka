users = ['Dave','Steve','Jackie']
data = [2 , False , 'Steve']

emptylist = []
print("Dave" in emptylist)
print(users[2])
print(users.index('Steve'))
users.append('Dicky')
print (users)

users.extend(['Mike'])
print(users)

users += ['Jason']
print(users)

users.insert(0, 'Bob')
print (users)

users[2:2] = ['Eddie', 'Alex']
print(users)

users[1:3] = ['Robert', 'JPJ']
print(users)

users.remove('Bob')
print(users)

print(users.pop())
print(users)

del users [0]
print(users)

data.clear()
print(data)

users[1:2] = ['dave']
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums = [4,43,55,11,32,90]

nums.sort(reverse=True)
print(nums)

print(sorted(nums, reverse = True))
print(nums)

numscopy= nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

#tuple
mytuple = (2,3,4,5)
Tuple = tuple((24,43,34,25))

print(mytuple)
print(Tuple)
print(type(mytuple))
print(type(Tuple))

newlist = list(mytuple)
print(newlist)
newlist.append('Neil')
newtuple = tuple(newlist)
print(newtuple)

(one, *two, hey) = Tuple
print(one)
print(hey)
print(two)