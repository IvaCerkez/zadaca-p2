import random

def parni_brojevi(brojevi):
    for broj in range(brojevi):
        if broj%2==0:
            yield broj

def neparni_brojevi(brojevi):
    for broj in range(brojevi):
        if broj%2!=0:
            yield broj

broj=random.randint(0, 100)
print(broj)

print("Parni brojevi: ", list(parni_brojevi(broj)))
print("Neparni brojevi: ", list(neparni_brojevi(broj)))
