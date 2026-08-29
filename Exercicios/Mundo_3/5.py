produtos = ('Iphone', 2000, 'Ipad', 4000, 'Macbook', 8000)

for lista in range(0, len(produtos), 2):
    print(f"{produtos[lista]:<10} {produtos[lista + 1] :>5}")



