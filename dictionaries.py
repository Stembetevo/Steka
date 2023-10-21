#Dictionaries
team = {
    "strikers":"Cristiano",
    "midfield":"DeBruyne"
}

team2 = {
    "strikers":"Haaland",
    "midfielders":"Reus"
}

print (type(team))
print(len(team2))

#Access items
print(team["strikers"])
print(team2.get("midfielders"))

#list all keys
print(team.keys())

#list all values
print(team2.values())

#list of key-values and pairs
print(team2.items())

#verify a key exists
print("strikers" in team2)
print("midfield" in team) 

#Change values
team["midfield"] = "Enzo"
team.update({"strikers":"Nkunku"})
print(team)

#Remove items
print(team.pop("strikers"))
print(team)

print(team.popitem())
print(team)

#del team2
team = team2.copy()
team2 ["strikers"] = "Lewandowski"
print(team)
print(team2)
#Best copy
team3 = dict(team)
print(team3)


##nested dictionaries

fifa1 = { 
    "chelseatm" : "Thiago",
    "manutm":"Rashford",
    "Liverpooltm":"Salah", 
}
fifa2 = {
    "RealM":"Bellingham",
    "Barcelona":"Pedri",
    "Atleti":"Griezman",
}

fifa3 = {
    "fifa1":fifa1,
    "fifa2":fifa2
}
print(fifa3)
print(fifa3["fifa2"]["Atleti"])

##Sets

nums = {1,2,3,4}
nums2 = set({1,2,3,4})
print(type(nums2))
print(type(nums))
print(len(nums2))
print(nums)
print(nums2)

#no duplicates are allowed

nums = {1,2,2,3,4}
print(nums)

#True is a dupe of 1 while false is a dupeof 0
nums = {True,3,4,False,2}
print(nums)
print(2 in nums)

#Adding items to a set
nums.add(8)
print(nums)

#Adding a set to another set
morenums = {67,23,22,55,65}
nums.update(morenums)
print(nums)

#merge sets
oldset = {1,2,3,4}
newset = {7,6,8,9}

mynewset = oldset.union(newset)
print(mynewset)

#Keep only the duplicate
one={1,2,3}
two={2,3,4}

one.intersection_update(two)
print(one)
one.symmetric_difference_update(two)
print(one)