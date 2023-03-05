cdd = str(input('Digite uma cidade: ')).strip()
cdd2 = cdd.lower()
cdd3 = cdd2.split()
print(f'A cidade de {cdd2.title()} possuí "santos" no começo do nome? {"santos" in cdd3 [0]}')