suma = 0

# Iterowanie po liczbach od 1 do 100
for i in range(1, 101):
    if i % 2 != 0:  # Sprawdzamy, czy liczba jest nieparzysta
        suma += i  # Dodajemy liczbę do sumy

# Wyświetlenie wyniku
print("Suma liczb nieparzystych od 1 do 100:", suma)
    
