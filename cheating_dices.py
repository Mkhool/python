from random import random
rnd = random()
if rnd < 0.1:
    print(1)
elif rnd < 0.2:
    print(2)
elif rnd < 0.3:
    print(3)
elif rnd < 0.4:
    print(4)
elif rnd < 0.5:
    print(5)
else:
    print(6)
    #50% de chance de tomber sur 6
print(rnd)
