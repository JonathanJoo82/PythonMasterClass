for i in range(1, 13):
    print("no. {0:2} squared is {1:4} and Cubed is {2:4}".format(i,i ** 2, i**3))

print()

for i in range(1, 13):
    print("no. {0:2} squared is {1:<3} and Cubed is {2:<4}".format(i,i ** 2, i**3))

print()

#decimal points
print("pi is about {0:12}".format(22/7))
print("pi is about {0:<12f}".format(22/7))
print("pi is about {0:12.50f}".format(22/7))
print("pi is about {0:<52.50f}".format(22/7))
print("pi is about {0:<62.50f}".format(22/7))
print("pi is about {0:<72.50f}".format(22/7))

print()
print("pi is about {0:12}".format(22/7))
print("pi is about {0:12f}".format(22/7))
print("pi is about {0:12.50f}".format(22/7))
print("pi is about {0:52.50f}".format(22/7))
print("pi is about {0:62.50f}".format(22/7))
print("pi is about {0:72.50f}".format(22/7))


print("pi is about {0:12.5f}".format(22/7))