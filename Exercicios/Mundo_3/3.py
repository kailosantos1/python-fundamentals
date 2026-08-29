import random

sorteador = tuple(random.sample(range(0,1000),5))

print(sorteador)
print(f"O maior numero e: {max(sorteador)}")
print(f"O menor numero e: {min(sorteador)}")