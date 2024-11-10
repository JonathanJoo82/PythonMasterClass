parrot ="Norwegian Blue"
print(parrot)
print(parrot[3])#print individual characters #w

#negative index
print(parrot[-3]) #l


print(parrot[1-3]) #evaluate the expression for this and use the value as the index point


#slicing or substring
print(parrot[0:6])
print(parrot[:6])
print(parrot[10:])
print(parrot[:])

print(parrot[-4:-2]) #Bl
print(parrot[-4:12]) #Bl



#using a step in slice.

print(parrot[0:6:2]) #Nre
print(parrot[0:6:3]) #Nw

#first line is starts at index position of 0.
#extends up to but not including the position 6.
#Step through the sequence in steps of 2.

print(parrot[0:7:2]) #Nrei

#slicing backwards
print(parrot[::-1])