import math
def encrypt(x):
    print(len(x))
    newstr = ""
    for i in range(int(math.ceil(len(x)/2))):
            newstr += str(x[i*2])
    if len(x) % 2 == 0:
        for i in range(int(len(x)/2)):
            newstr += str(x[2*i+1])
        return newstr
    for i in range(int(math.floor(len(x)/2))):
        newstr += str(x[(2*i)+1])
    return newstr

def decrypt(x):
    newstr = ""
    adder = 0
    if len(x) % 2 != 0:
        adder = 1
    for i in range(int(math.floor(len(x)/2))):
        offset = int(math.floor(len(x)/2))
        newstr += str(x[i]) + str(x[i+offset+adder])
    if len(x) % 2 != 0:
        newstr += x[int(math.floor(len(x)/2))]
    return newstr
print(decrypt("hloSmnSnh hnsaltfrraigti!!el io ig,tak  o o edn hs!"))
