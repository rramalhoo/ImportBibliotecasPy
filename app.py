import random

def sortear_numero(inicio, fim):
    numero = random.randint(inicio, fim)
    print(f"O numero sorteado foi {numero}")

sortear_numero(1, 10)
