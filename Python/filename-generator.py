import datetime

def filename_generator(const):
    return str(const+datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")+".txt")

#for example
data="IMG"
filename=filename_generator(data)

print(filename)
