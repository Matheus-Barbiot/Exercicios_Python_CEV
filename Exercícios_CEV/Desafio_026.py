frase = str(input('Digite uma frase: ')).strip()
print(f'Analizando a frase "{frase.capitalize()}"...')
print(f'A letra "A" aparece {frase.count("a") + frase.count("A")} vezes.')
low = frase.lower()
print(f'A letra "A" aparece pela primeira vez na posição {low.find("a") + 1}.')
print(f'A letra "A" aparece pela ultima vez na posição {low.rfind("a") + 1 }.')