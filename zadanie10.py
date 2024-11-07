 Zadanie:
# Napisz program, który wypisze wszystkie liczby od 1 do 50, które są liczbami pierwszymi.
# Liczba pierwsza to taka, która jest większa niż 1 i dzieli się tylko przez 1 i przez siebie.
# Program powinien wykorzystać pętlę i sprawdzenie, czy liczba jest pierwsza.

# A pod spodem rozwiązanie tego zadanka, napisane w Pythonie :)

# Funkcja sprawdzająca, czy liczba jest pierwsza
def czy_pierwsza(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Pętla wypisująca liczby pierwsze od 1 do 50
for num in range(1, 51):
    if czy_pierwsza(num):
        print(num)
