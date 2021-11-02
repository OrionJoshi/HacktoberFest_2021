# generate ip address
def genIp():
    import random
    rand=(random.sample(range(0,255),4))
    return "{}.{}.{}.{}".format(rand[0],rand[1],rand[2],rand[3])


for i in range(0,100):
    print(genIp())
