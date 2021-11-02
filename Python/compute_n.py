a = int(input("Enter an integer: "))
n1 = int( "%s" % a ) # %s signifies that you want to add a string value into a string
n2 = int( "%s%s" % (a,a))
n3 = int("%s%s%s" % (a,a,a))
print(n1+n2+n3)
